# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-06 22:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KSUvity', '0004_activity_actvimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='actvImage',
            new_name='activity_image',
        ),
    ]
