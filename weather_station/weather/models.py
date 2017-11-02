from django.db import models
from school.models import School
from datetime import datetime
# Create your models here.

class Weather(models.Model):
    created = models.DateTimeField()
    temperature = models.DecimalField(max_digits=3,decimal_places=1,default=None,null=True)
    humidity = models.DecimalField(max_digits=3,decimal_places=1,default=None,null=True)
    uv = models.IntegerField(default=None,null=True)
    light = models.IntegerField(default=None,null=True)
    rainfall = models.IntegerField(default=-1,null=True)
    school = models.ForeignKey(School,related_name='weathers',db_column='school',default=None,on_delete=models.CASCADE)

    def __str__(self):
        weather = '{0.temperature} {0.humidity} {0.uv} {0.light} {0.rainfall} {0.school}'
        #return weather.format(self)
        return weather.format(temperature,humidity,uv,light,rainfall ,school)
    class Meta:
        db_table='weather'

'''
from django.utils import timezone
Weather(timezone.now().strftime('%Y-%m-%d %H:%M:%S'),25,80,0,200,-1,1).save()
'''



    #之前沒有加str()出現TypeError: __repr__ returned non-string (type datetime.datetime)







#INSERT INTO weather_weather (time,temperature,humidity,uv,light,pm) values ('2017-08-29 20:50:40',25,77,0,3,2.5);




