# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160423_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]