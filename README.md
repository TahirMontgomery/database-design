# database-design

COP 4710 - Database Design Information System

To test API (ex.) http://localhost:8000/users/getUser)
$ cd API
$ python manage.py runserver

Making changes to API:
$ cd API
$ git add .
$ git commit -am "make it better"
$ git push heroku master

Superuser account (http://localhost:8000/admin/)
username: anagi
password: abc123

New model:
$ python manage.py makemigrations
$ python manage.py migrate

Frontend:
https://database-design-tahir-0429.web.app/