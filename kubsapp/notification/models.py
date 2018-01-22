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
    number = models.IntegerField(blank=False)
    title = models.CharField(max_length=50, blank=False)
    day = models.DateTimeField()
    image = models.ImageField()
    content = models.TextField(max_length=500, blank=False)
    #auth =