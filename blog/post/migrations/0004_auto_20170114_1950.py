# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170114_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]