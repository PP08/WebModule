import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "noisesearch",
        "USER": "phucphuong",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}