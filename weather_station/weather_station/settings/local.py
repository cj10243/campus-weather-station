from .base import *
import os
get_env_var('DJANGO_WEATHER_STATION_SECRET_KEY')
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
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        #'HOST': os.environ['DB_HOST'],   # Or an IP Address that your DB is hosted on
        'HOST': '203.72.63.54',
        'PORT': 3306,
    }
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