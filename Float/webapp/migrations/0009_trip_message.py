# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160618150656 on 2016-06-19 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_driver_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='message',
            field=models.CharField(default="Hello, let's be friends", max_length=800),
            preserve_default=False,
        ),
    ]
