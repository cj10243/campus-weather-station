from rest_framework import routers
from weather.api import Weather

v1 = routers.DefaultRouter()
v1.register(r'weather', t)