# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-31 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0012_auto_20181228_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='complaints',
            field=models.CharField(default='Enter Your complaints Here', max_length=100),
        ),
    ]
