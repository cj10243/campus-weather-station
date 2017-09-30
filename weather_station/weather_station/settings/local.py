from .base import *
import os
SECRET_KEY = 'ke67!frybp8=#&&n33m3l5tpc)#t9#rv@784z9)t&0crhl55@^'
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), #最原始的版本
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'), #添加local的版本
    }
}
'''

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
'''
#使用mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}
'''