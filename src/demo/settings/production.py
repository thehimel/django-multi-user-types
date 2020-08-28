# flake8: noqa
from .base import *

# In production, make sure environment variable DEBUG=False
DEBUG = config('DEBUG', cast=bool)

# Include your hosts here
ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': ''
    }
}

STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')
