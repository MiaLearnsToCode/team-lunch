from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# The context_object_name attribute on a generic view specifies the context variable to use
# INDEX
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
      return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:4]

# SHOW
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
      """
      Excludes any questions that aren't published yet.
      """
      return Question.objects.filter(pub_date__lte=timezone.now())

# RESULTS
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# function that adds one to the number of total votes of a choice each time the user selects it
def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
      selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
      return render(request, 'polls/detail.html', {
          'question': question,
          'error_message': "You didn't select a choice.",
      })
  else:
      selected_choice.votes += 1
      selected_choice.save()
      return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# After somebody votes in a question, the vote() view redirects to the results page for the question
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question': question})

