# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 10:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0053_gtask_lf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gtask',
            name='lf',
        ),
    ]
