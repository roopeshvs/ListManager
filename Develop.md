# List Manager

A List Manager Application created with Django.

## Packages Used

### djangorestframework

Django REST framework is a powerful and flexible toolkit for building Web APIs.

* We use this to create RESTful endpoints mentioned in the API documentation.

### django-rest-knox

Authentication Module for Django REST Authentication.

* We use this to create Tokens and Authenticate our RESTful endpoints.

### mysqlclient

MySQLClient provides Python 3 support for Python applications.

---

There are several apps under the List Manager project.

* todocrud - Settings & Base Files

* todos - List & List Item APIs

* accounts - User Accounts APIs

    Here, we utilise Django's existing User class by extending it by adding Date of Birth field.

* frontend - Contains ReactJS Files

    Note that all the JS files are compiled into one main.js file at frontend/static/main.js

---

## Commands

`python manage.py makemigrations` - Setup Database Changes from models.py across all apps

`python manage.py migrate` - Run The Database Changes

`python manage.py runserver` - Run The Application

`python manage.py createsuperuser` - Create Admin User

## Base Default URL Endpoints

http://localhost:8000 - Base User URL

http://localhost:8000/admin/ - Base Admin URL

## Updating JS Files

The applications directly only depend on the main.js file.

So, make sure your changes are reflected in the main.js file.

## API Endpoints

To read about the API endpoints, [click here](https://github.com/roopeshvs/ListManager/blob/master/API.md)
