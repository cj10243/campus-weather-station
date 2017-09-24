from django.shortcuts import render
from  weather.models import Weather
from django.views.generic.base import TemplateView

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