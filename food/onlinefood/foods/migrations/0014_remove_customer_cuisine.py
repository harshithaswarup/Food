# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-31 09:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0013_review_complaints'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cuisine',
        ),
    ]