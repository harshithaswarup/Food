# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-28 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0020_auto_20190123_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=5),
        ),
    ]
