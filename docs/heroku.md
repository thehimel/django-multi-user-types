# Heroku Deployment Process
- [Instructions](https://devcenter.heroku.com/articles/deploying-python)
- [Deploying to Heroku Server by Dennis Ivy](https://youtu.be/kBwhtEIXGII)
- [Heroku Postgres Connection by Dennis Ivy](https://youtu.be/TFFtDLZnbSs)

##  Files required
- runtime.txt
- requirements.txt
- Procfile

## Step 1: Gunicorn
Used to run the python server on deployment. [Doc](https://docs.gunicorn.org/en/latest/settings.html)
> In '--log-file -', FILE_NAME is '-'. It enables the gunicorn log to stderr.

`pip install gunicorn`

Create 'Procfile' with:
web: gunicorn project_name.wsgi --log-file -

## Step 2: settings.production
```python
DEBUG = False
ALLOWED_HOSTS = ['www.your-website.com', 'ip-address',]
```

## Step 3: .gitignore
Make sure .env is included in the .gitignore so that this file does't go to the deployment repository.
Also include .sqlite3 in the .gitignore.

## Step 4: Python Runtime
Check the Python version in your venv with `python --version` and add specify that in this file. It will let the Heroku server know which version of python to start with. Else, it will automatically select the latest available version.
Also check the heroku python runtime versions to match with your venv python version. After that decide the appropriate version.

[Link](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version)

runtime.txt
python-3.7.9

## Step 5: Static Files

### STATIC_ROOT
Define STATIC_ROOT in the project settings. It will allow WhiteNoise to perform the collectstatic command and save all the static files in this directory.
```python
STATIC_ROOT = BASE_DIR / 'static'
```
> STATICFILES_DIRS is used to let Django know what the directories to look for your static files. You save your necessary static files i.e. css, js, img, etc. in the STATICFILES_DIRS and STATIC_ROOT is used for collectstatic.


### Serving static files from Django with WhiteNoise. [Doc](http://whitenoise.evans.io/en/stable/)

`pip install whitenoise`

Edit your settings.py file and add WhiteNoise to the MIDDLEWARE list, above all other middleware apart from Django’s SecurityMiddleware:

```python
MIDDLEWARE = [
  # 'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  # ...
]
```

## Step 6 Heroku [Link](https://www.heroku.com/)
- Login to your Heroku account.
- Create an app.
- Copy the app url and add it to the ALLOWED_HOSTS in project settings.
- Set the env variable for db from the Postgres database given by Heroku.
- Select GitHub repo and deploy.
