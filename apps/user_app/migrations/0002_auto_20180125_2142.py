# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-25 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(default='description'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_level',
            field=models.IntegerField(default=2),
        ),
    ]
