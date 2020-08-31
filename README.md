# django-multi-user-types
A Django project that illustrates the implementation of multiple types of users.

## Important Package Versions
python==3.7
Django==3.1
django-allauth==0.42.0
django-crispy-forms==1.9.2

mdb==4.19.1
bootstrap==4


## Getting Started
Create and activate virtual env with Miniconda and install dependencies.
```bash
conda create --name mut python=3.7
conda activate mut
pip install -r requirements.txt
```

## Running the Server
Navigate inside directory src.
```bash
python manage.py runserver
```

## Changing Project Name
```bash
# Syntax: python manage.py rename <present_project_name> <new_project_name>
python manage.py rename demo my_project
```

## Generating SECRET_KEY

### Method 1
```bash
python manage.py shell
```
```python
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

### Method 2
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## User Types
A company having 2 types of users: Employee and Manager.

allauth has default SignupForm, SignupView. Do not override it. Let it be remain at accounts/signup. And do not change the signup form in the settings.py for allauth - it will override the save method and won't allow our employee and manager signup views to save anything extra.

We have customized the following files for the tasks below.
core/forms.py, core/views.py, templates/core/auth/signup.html

1. Employee
Create custom signup form for employee.
Create custom signup view for employee.
You must use a custom template in this signup view.

2. Manager
Create custom signup form for manager.
Create custom signup view for manager.
You must use a custom template in this signup view.

## Frontend
MDB-Free_4.19.1 with Boostrap 4 is used for frontend. [Link](https://mdbootstrap.com/docs/jquery/getting-started/download/)

Design of base.html
It was designed with the index.html file from mbd4 and allauth base.html.

Integrate MDB4 with all the html files inside templates/account.
The account folder is downloaded from the template directory of allauth github repository.

## Important Note
In the database, you must rename the site to include your site_name in emails.
You must change the default email_confirmation_subject. Changing a little bit will be enough. Otherwise it will add [example.com] in the subject.

'src\templates\account\email\email_confirmation_subject.txt'
Default: Please Confirm Your E-mail Address
Customized: Please Confirm The E-mail Address

## Renaming the Project
[Script]('./src/core/management/commands/rename.py')
Command
```bash
python manage.py rename current_project_name new_proejct_name
python manage.py rename demo my_project
```

## References
[GFG](https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/)
[pyblog](https://github.com/thehimel/pyblog)
[django-boilerplate](https://github.com/thehimel/django-boilerplate)
