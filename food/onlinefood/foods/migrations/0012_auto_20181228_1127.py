# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-28 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0011_auto_20181227_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.AddField(
            model_name='customer',
            name='Landmark',
            field=models.CharField(default='Near Billroth Hospital', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='Pincode',
            field=models.IntegerField(default=600028),
        ),
        migrations.AddField(
            model_name='customer',
            name='State',
            field=models.CharField(default='TN', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='area',
            field=models.CharField(default='Enter Area', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='house_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='customer',
            name='street_name',
            field=models.CharField(default='1st Main Road', max_length=50),
        ),
    ]
