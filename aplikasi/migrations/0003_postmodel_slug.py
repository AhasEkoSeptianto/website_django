# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-25 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikasi', '0002_auto_20200824_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
    ]