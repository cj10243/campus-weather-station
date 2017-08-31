from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from weather.serializers import WeatherSerializer
from .models import Weather

class WeatherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

