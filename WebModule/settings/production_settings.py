# """
# Django settings for WebModule project.
#
# Generated by 'django-admin startproject' using Django 1.10.6.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/1.10/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/1.10/ref/settings/
# """
#
# import os
#
# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'zxz^#oy&84n!!35t(i1^!&n+81*#9)su$!b#roc)7h54j4w)6$'
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
#
# ALLOWED_HOSTS = ['noisesearch.herokuapp.com']
#
# # Application definition
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'noisesearch',
#     'rest_framework',
#     'rest_framework.authtoken',
# ]
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'WebModule.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')]
#         ,
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'WebModule.wsgi.application'
#
# # Database
# # https://docs.djangoproject.com/en/1.10/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#     }
# }
#
# # Password validation
# # https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
# # Internationalization
# # https://docs.djangoproject.com/en/1.10/topics/i18n/
#
# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'Europe/Moscow'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.10/howto/static-files/
#
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#
# # redirect after login
# LOGIN_REDIRECT_URL = 'home'
# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
#
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.TokenAuthentication',
#         'rest_framework.permissions.AllowAny',
#     )
# }
#
# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)
#
# # Simplified static file serving.
# # https://warehouse.python.org/project/whitenoise/
#
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


"""
Django settings for WebModule project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zxz^#oy&84n!!35t(i1^!&n+81*#9)su$!b#roc)7h54j4w)6$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'noisesearch',
    'rest_framework',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'WebModule.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'WebModule.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'noisesearch',
        'USER': 'phucphuong',
        'PASSWORD': 'phucphuong',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# redirect after login
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.permissions.AllowAny',
    )
}

# SECRET_KEY = dj_database_url.config('zxz^#oy&84n!!35t(i1^!&n+81*#9)su$!b#roc)7h54j4w)6$')
DEBUG = dj_database_url.config('DEBUG', default=False)
DATABASES = {
    'default': dj_database_url.config(
        default=dj_database_url.config('DATABASE_URL')
    )
}