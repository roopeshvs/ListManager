# API Documentation

The Authorization Token for each user is generated at the time of login and deleted upon logout.

Package Used: django-rest-knox


## Authentication Endpoints

### Register User

POST http://127.0.0.1:8000/api/auth/register

Content-Type: application/json

{
    "first_name":"",
    "last_name":"",
    "username": "",
    "email": "",
    "password": "",
    "dob": ""
}

### Login User

POST http://127.0.0.1:8000/api/auth/login

Content-Type: application/json

{
    "username": "",
    "password": ""
}

### Logout User

POST http://127.0.0.1:8000/api/auth/logout

Authorization: Token


## List Endpoints

### Get All List Items

GET http://localhost:8000/api/todos/

Authorization: Token


### Get List Item by ID

GET http://localhost:8000/api/todos/{id}

Authorization: Token


### Delete List Item by ID

DELETE http://localhost:8000/api/todos/{id}

Authorization: Token


### Edit List Item by ID

PATCH http://localhost:8000/api/todos/{id}

Authorization: Token
