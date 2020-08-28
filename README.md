# List Manager

A List Manager Application created with Django.

## Live Application

Hosted at Python Anywhere

http://listmanager.pythonanywhere.com/

## Running List Manager Locally

### Installing Python

Please download Python 3.8 from https://www.python.org/downloads/

### Cloning the Repository

Clone this repository by running the command

`git clone https://github.com/roopeshvs/ListManager.git`

### Creating a Virtual Environment (Optional)

Create a Virtual Environment so that our dependencies are kept within this Environment and doesn't depend or affect the global packages.

Use the command `python -m venv VENV` or `python3 -m venv VENV`, depending on your operating system.

### Activating a Virtual Environment (Optional)

For Linux Bash, use
`VENV/bin/activate`

For Windows Command Prompt, use
`VENV\Scripts\activate.bat`

### Installing Dependencies

Install the required dependencies by running the command, from root,
`pip install -r requirements.txt`

### Setting Up The Database

In settings.py, change the Database Settings.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'YOUR-DB-NAME-GOES-HERE',
        'USER': 'YOUR-DB-USER-NAME-GOES-HERE',
        'PASSWORD': 'YOUR-DB-PASSWORD-NAME-GOES-HERE',
        'HOST': 'localhost',
        'PORT': '3306', #Default PORT
    }
}
```

To create tables in your database, run the commands

For Linux, use

`python3 manage.py makemigrations`

`python3 manage.py migrate`

For Windows, use

`python manage.py makemigrations`

`python manage.py migrate`

### Create a Super User (Admin):

Create a Super User, who will be the admin for our site, using the command,

`python3 manage.py createsuperuser` or `python manage.py runserver`

### You Are All Set!

To start the server, run the command

For Linux, use

`python3 manage.py runserver`

For Windows, use

`python manage.py runserver`

Head over to http://localhost:8000/ to use the List Manager.