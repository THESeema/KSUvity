# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-16 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KSUvity', '0005_auto_20171206_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_image',
            field=models.ImageField(upload_to=b'pic_folder/'),
        ),
    ]
