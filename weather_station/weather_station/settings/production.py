from .base import *

DEBUG = False

SECRET_KEY = get_env_var('DJANGO_WEATHER_STATION_SECRET_KEY')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weatherstation',
        'USER': get_env_var('DJANGO_WEATHER_STATION_DATABASE_DEFAULT_USER'),
        'PASSWORD': get_env_var('DJANGO_WEATHER_STATION_DATABASE_DEFAULT_PASSWORD'),
        'HOST': get_env_var('DJANGO_WEATHER_STATION_DATABASE_DEFAULT_HOST'),
        'PORT': '',
    },
}

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')