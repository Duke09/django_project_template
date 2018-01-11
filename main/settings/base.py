"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.realpath(os.path.dirname(__file__) + "/.."))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*po#e#9e277)@@b$dnc=ai1w#!49-g_%v^xa3!6twpr!rwj$g('


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
    'simple_django_logger',
    'ckeditor',
    'kv_settings',
    'corsheaders',
    'django_user_agents',
    'djcelery',
    'django.contrib.humanize',
    'appauth',
    'app_meta',
    'posts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Ensure CorsMiddleware is above CommonMiddleware
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'simple_django_logger.middleware.errormiddleware.ErrorMiddleware',
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


# WSGI_APPLICATION = 'main.wsgi.application'


# Tells which model to use as primary User
AUTH_USER_MODEL = 'appauth.AppUser'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

VERSION = {
    'v1': '0.1',
}

LOGIN_URL = '/admin/login/'
LOGOUT_URL = '/admin/logout/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
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


# List of site admins
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('John Doe', 'johndoe@gmail.com'),
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
# task result life time until they will be deleted
CELERY_TASK_RESULT_EXPIRES = 7 * 86400  # 7 days
# needed for worker monitoring
CELERY_SEND_EVENTS = True
# where to store periodic tasks (needed for scheduler)
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"


# add following lines to the end of settings.py
import djcelery
djcelery.setup_loader()
