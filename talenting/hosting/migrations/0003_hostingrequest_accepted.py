# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0002_auto_20171214_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostingrequest',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]