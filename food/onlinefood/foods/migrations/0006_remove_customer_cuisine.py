# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-26 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_auto_20181226_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cuisine',
        ),
    ]
