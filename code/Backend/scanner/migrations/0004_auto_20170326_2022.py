# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-26 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0003_auto_20170326_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='Time',
            field=models.TimeField(),
        ),
    ]