# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20170114_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
