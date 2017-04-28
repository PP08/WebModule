import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'noisesearch',
        'USER': 'phucphuong',
        'PASSWORD': '',
        'PORT': '5342',
    }
}

DEBUG = True