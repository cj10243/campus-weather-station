json_file = [
    {
        "model": "weather.weather",
        "pk": 1,
        "fields": {
            "time": "2017-09-02T00:54:27Z",
            "temperature": "31.5",
            "humidity": "71.5",
            "uv": 0,
            "light": 751,
            "rainfall": -1,
            "school": 1
        }
    },
    {
        "model": "weather.weather",
        "pk": 2,
        "fields": {
            "time": "2017-09-01T23:59:27Z",
            "temperature": "31.5",
            "humidity": "71.5",
            "uv": 0,
            "light": 751,
            "rainfall": -1,
            "school": 2
        }
    },
    {
        "model": "weather.weather",
        "pk": 3,
        "fields": {
            "time": "2017-09-02T00:04:27Z",
            "temperature": "31.5",
            "humidity": "71.5",
            "uv": 0,
            "light": 751,
            "rainfall": -1,
            "school": 3
        }
    }]
import json
from pprint import pprint
with open("weather_station.json","r") as f:
        data = json.load(f)
        print("加载入文件完成...")
pprint(data)


from weather.models import Weather
from school.models import School



for i in json_file:
    school = School.objects.all()[0]
    Weather(time="{}".format(i['fields']['time']),
            temperature="{}".format(i['fields']['temperature']),
            humidity="{}".format(i['fields']['humidity']),
            uv="{}".format(i['fields']['uv']),
            light="{}".format(i['fields']['light']),
            rainfall="{}".format(i['fields']['rainfall']),
            school=school).save()


#exec(open('test_script.py',encoding='utf8').read())
'''