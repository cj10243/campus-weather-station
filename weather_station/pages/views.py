from django.shortcuts import render
from  weather.models import Weather
from school.models import School
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(TemplateView):
    template_name = "pages/home.html"

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        temperature = [Weather.objects.order_by('-time')[i].temperature for i in range(287)][::-1]
        print(temperature)
        humidity = [Weather.objects.order_by('-time')[i].humidity for i in range(287)][::-1]
        uv = [Weather.objects.order_by('-time')[i].uv for i in range(287)][::-1]
        light = [Weather.objects.order_by('-time')[i].light for i in range(287)][::-1]
        rainfall = [Weather.objects.order_by('-time')[i].rainfall for i in range(287)][::-1]
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


class StatusView(TemplateView):
    template_name = "pages/status.html"
    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)
        schools = School.objects.all()

        #context['weathers'] =  [Weather.objects.filter(school=i+1).order_by('-time')[0] for i in range(0,len(schools))]
        context['weather'] = []
        context['temperature'] = []
        context['humidity'] = []
        context['uv'] = []
        context['light'] = []
        context['rainfall'] = []
        context['weathers'] = []
        for i in range(0,len(schools)):
            weathers_order_by_time = Weather.objects.filter(school=i+1).order_by('-created')
            context['weather'].append(weathers_order_by_time[0])
            context['temperature'].append([float(i.temperature) for i in weathers_order_by_time])
            context['humidity'].append([i.humidity for i in weathers_order_by_time])
            context['uv'].append([i.uv for i in weathers_order_by_time])
            context['light'].append([i.light for i in weathers_order_by_time])
            context['rainfall'].append([i.rainfall for i in weathers_order_by_time])


        # context['chart'] = {"renderTo":context['chartID'], "type": "line", "height": 500,}
        # context['series'] = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
        # context['title'] = {"text": 'My Title'}
        # context['xAxis'] = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
        # context['yAxis'] = {"title": {"text": 'yAxis Label'}}
        return context

class AboutView(TemplateView):
    template_name = "pages/about.html"


