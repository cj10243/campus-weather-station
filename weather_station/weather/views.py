from rest_framework import viewsets
from weather.serializers import WeatherSerializer
from .models import Weather
from rest_framework import filters

class WeatherViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('time' ,'temperature','humidity' ,'uv' ,'light','rainfall','school_id')
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    lookup_field = "school_id"

