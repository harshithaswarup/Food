# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-14 11:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0013_auto_20190114_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='food',
            name='food_name',
        ),
        migrations.RemoveField(
            model_name='food',
            name='rate',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]
