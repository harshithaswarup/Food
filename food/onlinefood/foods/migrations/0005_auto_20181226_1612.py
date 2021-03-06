# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-26 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_auto_20181226_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cuisine',
            field=models.BooleanField(choices=[('V', 'Veg'), ('NV', 'NonVeg')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='remember',
            field=models.BooleanField(default=True),
        ),
    ]
