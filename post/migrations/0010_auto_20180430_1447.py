# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-04-30 05:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20180426_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.Post'),
        ),
    ]
