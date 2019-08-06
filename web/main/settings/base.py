"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.realpath(os.path.dirname(__file__) + "/.."))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'ckeditor',
    'widget_tweaks',
    'corsheaders',
    'django_user_agents',
    'django_celery_results',
    'django_celery_beat',
    'django.contrib.humanize',
    'appauth',
    'posts',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Ensure CorsMiddleware is above CommonMiddleware
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
)

ROOT_URLCONF = 'main.urls'

# Template paths
# Absolute path to the templates directory
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            TEMPLATE_PATH,
        ],
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


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT']
    }
}


WSGI_APPLICATION = 'main.wsgi.application'


# Tells which model to use as primary User
AUTH_USER_MODEL = 'appauth.AppUser'


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
CELERY_TIMEZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

VERSION = {
    'v1': '0.1',
}


# AWS Settings
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_ACCESS_SECRET']
AWS_REGION_NAME = os.environ['AWS_REGION']

LOGIN_URL = '/admin/login/'
LOGOUT_URL = '/admin/logout/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
# Give absolute directory while in production. This is where all static files will reside
# STATIC_ROOT = ''   STATIC_ROOT can be found in respective setting files
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATIC_PATH = os.path.join(BASE_DIR, 'site_static')    # Absolute path to the static directory
STATICFILES_DIRS = (
    STATIC_PATH,
)


# CORS related settings

# Change this in production! And use the following
# CORS_ORIGIN_WHITELIST = (
#         'google.com',
#         'hostname.example.com'
#     )
# https://github.com/ottoyiu/django-cors-headers/
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'sessionid',
)
CORS_EXPOSE_HEADERS = (
    'set-cookie',
    'sessionid',
    'csrftoken',
)


# Celery related settings
CELERY_INCLUDE = (
    'global_tasks.email_tasks.email_tasks', )
CELERY_RESULT_BACKEND = 'django-cache'
CELERY_BROKER_URL = 'redis://redis:6379/0'
# Using pickle for serializing instead of JSON because
# it supports serializing python objects
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_ACCEPT_CONTENT = ['pickle']


# Email server settings
# ABSOLUTELY REMOVE THE DUMMY EMAIL SERVER IN PRODUCTION!!!
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_FROM = os.environ['EMAIL_FROM']