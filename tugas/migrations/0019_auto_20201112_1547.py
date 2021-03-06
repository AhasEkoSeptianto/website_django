# Generated by Django 3.1.3 on 2020-11-12 15:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tugas', '0018_auto_20200925_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='publish',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
