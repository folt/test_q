# -*- coding: utf-8 -*-
from server.settings.components import config

CACHE_DEFAULT_HOST = config('CACHE_DEFAULT_HOST')
CACHE_DEFAULT_PORT = config('CACHE_DEFAULT_PORT', cast=int)
CACHE_DEFAULT_DB = config('CACHE_DEFAULT_DB', cast=int)

# Caching
CACHES = {
    'default':
        {
            'BACKEND': 'django_redis.cache.RedisCache',
            'TIMEOUT': 5,
            'LOCATION': f'redis://{CACHE_DEFAULT_HOST}:{CACHE_DEFAULT_PORT}/{CACHE_DEFAULT_DB}',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient'}
        },
}
