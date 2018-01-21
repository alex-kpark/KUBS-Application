# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField('USERNAME', max_length=50)
    studentid = models.IntegerField('STUDENRID', max_length=10)
    password = models.CharField('PASSWORD', max_length=20)
    email = models.CharField('EMAIL', max_length=20)
    