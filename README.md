# django-multi-user-types
A Django project that illustrates the implementation of multiple types of users.

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

## References
[GFG](https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/)
