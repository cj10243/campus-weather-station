from django.shortcuts import render
from  weather.models import Weather
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = "pages/home.html"

class StatusView(TemplateView):
    template_name = "pages/status.html"

    def weathers(self):
        return Weather.objects.all()

class AboutView(TemplateView):
    template_name = "pages/about.html"