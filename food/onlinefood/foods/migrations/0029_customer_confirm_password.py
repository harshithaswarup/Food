# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-30 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0028_auto_20190130_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='confirm_password',
            field=models.CharField(default='harshi', max_length=10),
        ),
    ]
