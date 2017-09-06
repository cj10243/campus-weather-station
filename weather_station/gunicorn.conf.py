import os

bind = '203.72.63.200:8000'
worders = (os.sysconf('SC_NPROCESSORS_ONLN') * 2) + 1
loglevel = 'error'
command = '/home/nhcc/venv/weather_station/bin/gunicorn'
pythonpath = '/home/nhcc/campus-weather-station/weather_station'

