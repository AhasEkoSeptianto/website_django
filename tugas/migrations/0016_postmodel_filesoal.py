# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-25 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tugas', '0015_auto_20200925_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='Filesoal',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
