# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 05:56
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hosting', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('recommendations', models.IntegerField(default=0)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_host', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GuestReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('recommend', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='MyTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('arrival_date', models.DateField()),
                ('departure_date', models.DateField()),
                ('number_travelers', models.IntegerField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='profile')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=6)),
                ('self_intro', models.TextField(blank=True)),
                ('talent_category', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), null=True, size=None)),
                ('talent_intro', models.TextField(blank=True)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('occupation', models.CharField(blank=True, max_length=20)),
                ('available_languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), null=True, size=None)),
            ],
        ),
        migrations.AddField(
            model_name='mytrip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='guestreview',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review_about_guest', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='guestreview',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review_by_host', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='wish_event',
            field=models.ManyToManyField(related_name='wish_event', to='event.Event'),
        ),
        migrations.AddField(
            model_name='user',
            name='wish_hosting',
            field=models.ManyToManyField(related_name='wish_hosting', to='hosting.Hosting'),
        ),
        migrations.AddField(
            model_name='profileimage',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='member.Profile'),
        ),
        migrations.AddField(
            model_name='user',
            name='wish_profile',
            field=models.ManyToManyField(related_name='wish_profile', to='member.Profile'),
        ),
    ]
