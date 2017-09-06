from django.db import models

# Create your models here.

class Weather(models.Model):
    time = models.DateTimeField()
    temperature = models.DecimalField(max_digits=3,decimal_places=1)
    humidity = models.DecimalField(max_digits=3,decimal_places=1)
    uv = models.IntegerField()
    light = models.IntegerField()
    rainfall = models.DecimalField(max_digits=2,decimal_places=1)

    def __str__(self):
        weather = '{0.time} {0.temperature} {0.humidity} {0.uv} {0.light} {0.rainfall}'
        return weather.format(self)


    #之前沒有加str()出現TypeError: __repr__ returned non-string (type datetime.datetime)






#INSERT INTO weather_weather (time,temperature,humidity,uv,light,pm) values ('2017-08-29 20:50:40',25,77,0,3,2.5);




