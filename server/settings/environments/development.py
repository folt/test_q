# -*- coding: utf-8 -*-


"""
This file contains all the settings that defines the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

from typing import List

from server.settings.components import config, BASE_DIR
from server.settings.components.common import INSTALLED_APPS, MIDDLEWARE

# Setting the development status:

DEBUG = True

ALLOWED_HOSTS = [
    config('DOMAIN_NAME'),
]

# Static files:
# https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-STATICFILES_DIRS
STATIC_URL = config('CDN_HOST')

# Installed apps for developement only:

INSTALLED_APPS += (
    'debug_toolbar',
)

# Static files:
# https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-STATICFILES_DIRS

STATICFILES_DIRS: List[str] = []


# Django debug toolbar:
# https://django-debug-toolbar.readthedocs.io

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


def custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    return request.user.is_superuser


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK':
        'server.settings.environments.development.custom_show_toolbar',
}
