from .base import *

DEBUG = True

SECRET_KEY = get_env_var('DJANGO_WEATHER_STATION_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weatherstation_test',
        'USER': get_env_var('DJANGO_WEATHER_STATION_DATABASE_DEFAULT_USER'),
        'PASSWORD': get_env_var('DJANGO_WEATHER_STATION_DATABASE_DEFAULT_PASSWORD'),
        'HOST': get_env_var('DJANGO_WEATHER_STATION_DATABASE_DEFAULT_HOST'),
        'PORT': '3306',
    },
}

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
