# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-18 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0018_auto_20190117_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
