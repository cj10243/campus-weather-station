    import os

    bind = '127.0.0.1:8080'
    worders = (os.sysconf('SC_NPROCESSORS_ONLN') * 2) + 1
    loglevel = 'error'
    command = '/home/nhcc/venv/weather_station/bin/gunicorn'
    pythonpath = '$project/weather_station'