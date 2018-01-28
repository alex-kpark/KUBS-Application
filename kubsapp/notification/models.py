# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Student(models.Model):
    username = models.CharField(max_length=30, blank=False)
    studentid = models.CharField(max_length=10, blank=False)
    password = models.CharField(max_length=40, blank=False)
    email = models.CharField(max_length=50, blank=False)
    #follow =
    #auth =


class Notice(models.Model):
    number = models.IntegerField(blank=False, null=True)
    title = models.CharField(max_length=50, blank=False)
    day = models.DateTimeField(null=False)
    image = models.ImageField(null=False)
    content = models.TextField(max_length=500, blank=False, null=False)
    auth = models.IntegerField(blank=False, default=1, null=False)