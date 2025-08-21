from email.policy import default

from .common import *
from decouple import config,Csv

SECRET_KEY = config("PROD_SECRET_KEY",cast=str)
DEBUG = config("DEBUG",default=False,cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS",cast=Csv)


WSGI_APPLICATION = 'core.wsgi.prod.application'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME",cast=str),
        "USER": config("DB_USER",cast=str),
        "PASSWORD": config("DB_PASSWORD",cast=str),
        "HOST": config("DB_HOST",cast=str),
        "PORT": config("DB_PORT",cast=str),
    }
}



