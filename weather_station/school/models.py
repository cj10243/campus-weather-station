from django.db import models
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=10,null=False)
    eng_name = models.CharField(max_length=50,null=False)
    school_abbreviation= models.CharField(max_length=8,null=False)


    def __str__(self):
        school = '{0.name} {0.eng_name} {0.school_abbreviation}'
        return school.format(self)

    class Meta:
        db_table='school'
    #[School.objects.filter(id=i).update(weather_id=i) for i in range(1,2837)]
    #[School(name="臺北市立內湖高中",eng_name="Taipei Municipal Nei-Hu Senior High School",weather_id=i).save() for i in range(1,2837)]
    #[School(name="國立華僑高中",eng_name="National Overseas Chinese Senior High School",weather_id=i).save() for i in range(1,2837)]
#[Weather.objects.filter(id=i).update(school=a) for i in range(1,2837)]
'''
School(1,"臺北市立內湖高級中學","Taipei Municipal Neihu High School","nhsh").save()
School(2,"國立華僑高級中學","National Overseas Chinese Senior High School","nocsh").save()
School(3,"臺北市立中山女高","Taipei Municipal Zhongshan Girls High School","csghs").save()
School(4,"臺北市立景美女中","Taipei Municipal Jingmei Girls' High School","cmgsh").save()
'''