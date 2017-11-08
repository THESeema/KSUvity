# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-01 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KSUvity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='attendee',
            field=models.ManyToManyField(null=True, related_name='attendees', to='KSUvity.Attendee'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='volunteer',
            field=models.ManyToManyField(null=True, related_name='volunteers', to='KSUvity.Volunteer'),
        ),
    ]
