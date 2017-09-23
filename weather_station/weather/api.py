from rest_framework import viewsets, serializers, permissions
from .models import Weather

class MenuItemRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('time' ,'temperature','humidity' ,'uv' ,'light','rainfall')