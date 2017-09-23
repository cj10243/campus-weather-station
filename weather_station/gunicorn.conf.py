# -*- coding: utf-8 -*-
# /usr/bin/python3
import os

bind = '{}:8000'.format(os.environ['DJANGO_WEATHER_STATION_HOST'])
worders = (os.sysconf('SC_NPROCESSORS_ONLN') * 2) + 1
loglevel = 'error'
command = "WTR_VENV/gunicorn"
pythonpath = "$PROJECT/weather_station"

