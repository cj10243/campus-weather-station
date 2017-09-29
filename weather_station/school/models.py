from django.db import models
from weather.models import Weather
# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=10,null=False)
    eng_name = models.CharField(max_length=50,null=False)
    school_id = models.CharField(max_length=8,null=False)
    weather = models.ForeignKey(Weather,related_name="school",on_delete=models.CASCADE)

    def __str__(self):
        school = '{0.name} {0.eng_name} {0.school_id}'
        return school.format(self)

    #[School.objects.filter(id=i).update(weather_id=i) for i in range(1,2837)]
    #[School(name="臺北市立內湖高中",eng_name="Taipei Municipal Nei-Hu Senior High School",weather_id=i).save() for i in range(1,2837)]
    #[School(name="國立華僑高中",eng_name="National Overseas Chinese Senior High School",weather_id=i).save() for i in range(1,2837)]