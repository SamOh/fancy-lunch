# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='distance',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
