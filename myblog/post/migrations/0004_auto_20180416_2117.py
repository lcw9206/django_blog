# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-04-16 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20180413_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=150, verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='제목'),
        ),
    ]
