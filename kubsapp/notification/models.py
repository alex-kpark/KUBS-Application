# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Student(models.Model):
    username = models.CharField(max_length=30, blank=False)
    studentid = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=False)
    # follow = models.
    # repre = models.IntegerField(blank=False, default=1, null=False) #representative - check whether it has right to post it or not

class Notice(models.Model):
    number = models.IntegerField(blank=False, null=True)
    title = models.CharField(max_length=50, blank=False)
    day = models.DateTimeField(null=False)
    image = models.ImageField(null=False)
    content = models.TextField(max_length=500, blank=False, null=False)
    # author = models.IntegerField(blank=False, default=1, null=False) #Check who is the author of the post