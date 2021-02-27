# -*- coding: utf-8 -*-
import os

from typing import Tuple

from server.settings.components import BASE_DIR, config

SECRET_KEY = config('DJANGO_SECRET_KEY')

SMS_TEST_MODE = False
IS_LOCAL = False
DEBUG = False

# Application definition:
INSTALLED_APPS: Tuple[str, ...] = (

    # Default django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Rest:
    'rest_framework',

    'rest_auth',

    # Security:
    'corsheaders',

    # Extra:
    'django_extensions',

    # Common:

    # Your apps go here:
    'server.apps.core',

)

MIDDLEWARE: Tuple[str, ...] = (
    # Content Security Policy:
    'corsheaders.middleware.CorsMiddleware',

    # Django:
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'server.urls'
AUTH_USER_MODEL = 'core.Customers'
WSGI_APPLICATION = 'server.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('DJANGO_DATABASE_HOST'),
        'PORT': config('DJANGO_DATABASE_PORT', cast=int),
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': config('CONN_MAX_AGE', cast=int, default=60),
        'OPTIONS': {
            'connect_timeout': 10,
        },
    }
}


# Internationalization
LANGUAGE_CODE = 'ru-RU'

USE_I18N = True
USE_L10N = True

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)

LOCALE_PATHS = (
    'locale/',
)

USE_TZ = True
TIME_ZONE = 'Europe/Moscow'


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Templates
TEMPLATES = [{
    'APP_DIRS': True,
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        # Contains plain text templates, like `robots.txt`:
        BASE_DIR.joinpath('server', 'templates'),
    ],
    'OPTIONS': {
        'context_processors': [
            # Default template context processors:
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.request',
        ],
    },
}]


# Media files
# Media root dir is commonly changed in production
# (see development.py and production.py).
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')


# Django authentication system
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]


# Security
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
