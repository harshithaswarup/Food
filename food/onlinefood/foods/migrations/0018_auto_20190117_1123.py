# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-17 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0017_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='area',
            field=models.CharField(default='R.A Puram', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='house_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='Rakhi', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(default='rakhi@example.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='food',
            name='cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='rate',
            field=models.IntegerField(),
        ),
    ]
