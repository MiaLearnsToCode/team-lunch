from django.contrib import admin
from django.urls import include, path

#  Pointing the root URLconf at the polls.urls module

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
