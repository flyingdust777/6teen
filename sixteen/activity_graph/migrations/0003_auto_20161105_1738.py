# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-05 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_graph', '0002_auto_20161105_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(default='Business Name', max_length=250),
        ),
    ]