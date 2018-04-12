# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-04-12 09:06
from __future__ import unicode_literals

import accounts.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180412_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='media/images/default.jpeg', upload_to=accounts.models.set_image_path),
        ),
    ]
