"""
Django settings for TwigYourHealth project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

from private_settings import *


def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)


BASE_DIR = rel('.')
DEBUG = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!

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
    'sass_processor',
    'phonenumber_field',
    'annoying',
    'material',
    'material.frontend',
    'mptt',
    'channels',
    'sorl.thumbnail',
    "storages",

    'accounts',
    'notifications',
    'communication',
    'deceases',
    'timetables',
    'payments',
    'utils',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'accounts.middleware.LoginRequiredMiddleware'
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [rel('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'communication.context_processors.chats',
                'notifications.context_processors.notifications',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

# Database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
#  DEV
AUTHENTICATION_BACKENDS = ['accounts.backend.EmailPhoneUsernameBackend']
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/accounts/login/'
LOGIN_EXEMPT_URLS = ['admin/', 'accounts/sign-up/', 'contact/', 'about/']
AUTH_USER_MODEL = 'accounts.User'
LOCALE_PATHS = (rel('..', 'locale'),)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_ROOT = rel('..', 'files', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = rel('..', 'files', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    rel('static'),
)


SASS_PROCESSOR_INCLUDE_DIRS = [
    rel('..', 'files', 'static', 'scss'),
]
SASS_PROCESSOR_ROOT = rel('..', 'static')

FIXTURE_DIRS = [rel('fixtures')]

# CMS
# PB = Pushbullet(PUSHBULLEY_KEY)

# Chat
ASGI_APPLICATION = "routing.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

CORS_ORIGIN_ALLOW_ALL = True
