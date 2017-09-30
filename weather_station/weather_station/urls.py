from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from weather import views

router = routers.DefaultRouter()
router.register(r'weathers', views.WeatherViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'weather_station.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('pages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls,namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]
