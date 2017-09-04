# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_weather'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='pm',
        ),
        migrations.AddField(
            model_name='weather',
            name='rainfall',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
    ]
