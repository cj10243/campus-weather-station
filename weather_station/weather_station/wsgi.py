"""
WSGI config for weather_station project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather_station.settings.production")
<<<<<<< HEAD
=======
from dj_static import Cling

application = Cling(get_wsgi_application())
>>>>>>> e487ef98e1453eaec13b0c4aea851be16bcbc84c

