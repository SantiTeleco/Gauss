# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0006_auto_20160321_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='gday',
            name='gtime_slots',
            field=models.ManyToManyField(blank=True, to='gprojects.Gtime_slot'),
        ),
    ]
