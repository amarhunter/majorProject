# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-04-01 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIS', '0012_auto_20160802_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(choices=[('Computer Science & Engineering', 'Computer Science & Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Others', 'Others')], default='Computer Science & Engineering', max_length=100),
        ),
    ]
