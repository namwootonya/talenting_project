# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-13 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20171212_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='primary_photo',
            field=models.ImageField(max_length=255, upload_to='event'),
        ),
    ]