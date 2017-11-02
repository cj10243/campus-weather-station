from rest_framework import viewsets
from weather.serializers import WeatherSerializer
from .models import Weather
from rest_framework import filters,pagination


class WeatherViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('time' ,'temperature','humidity' ,'uv' ,'light','rainfall','school')
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    lookup_field = "school"
    pagination.PageNumberPagination.pages_size = 100
    pagination.PageNumberPagination.paginate_by_param = 'pages_size'

