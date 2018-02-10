# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-10 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20180210_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='author',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='student',
            name='follow',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]