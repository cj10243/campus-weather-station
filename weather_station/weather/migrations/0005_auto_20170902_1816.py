# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_auto_20170903_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='humidity',
            field=models.DecimalField(decimal_places=1, default=None, max_digits=3),
        ),
        migrations.AlterField(
            model_name='weather',
            name='light',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='weather',
            name='rainfall',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='weather',
            name='temperature',
            field=models.DecimalField(decimal_places=1, default=None, max_digits=3),
        ),
        migrations.AlterField(
            model_name='weather',
            name='uv',
            field=models.IntegerField(default=None),
        ),
    ]
