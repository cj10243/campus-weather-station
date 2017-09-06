from django.shortcuts import render
from  weather.models import Weather
# Create your views here.
def home(request):
    weather = Weather.objects.all()

    return render(request, 'pages/home.html',{'weather': weather})
def status(request):
    weather = Weather.objects.all()
    return render(request, 'pages/home.html', {'weather': weather})