# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-10 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_auto_20180210_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='id',
        ),
        migrations.AlterField(
            model_name='notice',
            name='number',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]