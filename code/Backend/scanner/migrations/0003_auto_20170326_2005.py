# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-26 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0002_auto_20170326_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Date',
            field=models.CharField(max_length=250),
        ),
    ]
