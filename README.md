## Set Up
$ pip install Django
$ django-admin startproject mysite

inside of mysite:
$ python manage.py runserver <----
$ python manage.py startapp polls

create the tables in the database:
$ python manage.py migrate
$ python manage.py makemigrations polls

the sqlmigrate command takes migration names and returns their SQL:
$ python manage.py sqlmigrate polls 0001

run migrate again to create those model tables in your database:
$ python manage.py migrate

## More instructions
- Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database.

## Super User:
$ python manage.py createsuperuser
http://127.0.0.1:8000/admin/

## Tests
$ python manage.py test polls <----
