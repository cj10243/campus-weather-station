from django.conf.urls import include, url
from django.contrib import admin
from pages.views import home
from chart.views import status
from rest_framework import routers
from weather import views

router = routers.DefaultRouter()
router.register(r'weathers', views.WeatherViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'weather_station.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home, name='home'),
    url(r'^status/$', status, name='draw'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]
