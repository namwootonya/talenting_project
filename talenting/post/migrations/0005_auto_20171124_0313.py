# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 03:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20171124_0309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='description',
            old_name='hosting',
            new_name='place',
        ),
    ]