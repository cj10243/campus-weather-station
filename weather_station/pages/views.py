from django.shortcuts import render
from  weather.models import Weather
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(TemplateView):
    template_name = "pages/home.html"

class StatusView(TemplateView):
    template_name = "pages/status.html"
    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)
        context['weathers'] = Weather.objects.all()
        return context
    '''
    def weathers(self):
        return Weather.objects.order_by().all()[0]
'''
class AboutView(TemplateView):
    template_name = "pages/about.html"

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        temperature = [Weather.objects.order_by('-time')[i].temperature for i in range(287)]
        humidity = [Weather.objects.order_by('-time')[i].humidity for i in range(287)]
        uv = [Weather.objects.order_by('-time')[i].uv for i in range(287)]
        light = [Weather.objects.order_by('-time')[i].light for i in range(287)]
        rainfall = [Weather.objects.order_by('-time')[i].rainfall for i in range(287)]

        labels = ["Temperature", "Humidity", "UV", "Light", "RainFall"]
        data = {
            "temperature": temperature,
            "humidity": humidity,
            "uv": uv,
            "light": light,
            "rainfall": rainfall,
            "labels": labels,
        }
        return Response(data,template_name='pages/status.html')