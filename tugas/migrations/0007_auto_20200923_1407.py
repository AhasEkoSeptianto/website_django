# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-23 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tugas', '0006_postmodel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='Pertemuan',
            field=models.CharField(choices=[('Pertemuan01', 'Pertemuan01'), ('Pertemuan02', 'Pertemuan02'), ('Pertemuan03', 'Pertemuan03'), ('Pertemuan04', 'Pertemuan04'), ('Pertemuan05', 'Pertemuan05'), ('Pertemuan06', 'Pertemuan06'), ('Pertemuan07', 'Pertemuan07'), ('Pertemuan08', 'Pertemuan08'), ('Pertemuan09', 'Pertemuan09'), ('Pertemuan10', 'Pertemuan10'), ('Pertemuan11', 'Pertemuan11'), ('Pertemuan12', 'Pertemuan12'), ('Pertemuan13', 'Pertemuan13'), ('Pertemuan14', 'Pertemuan14'), ('Pertemuan15', 'Pertemuan15'), ('Pertemuan16', 'Pertemuan16')], default='Pertemuan1', max_length=20),
        ),
    ]
