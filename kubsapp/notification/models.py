# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.


class Student(models.Model):
    username = models.CharField(max_length=30, blank=False)
    studentid = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=False)
    follow = models.CharField(max_length=200, blank=False)
    # representative - check whether it has right to post it or not
    represent = models.CharField(max_length=200, blank=False, default=99, null=False)

    def __str__(self):
        return str(self.studentid)


class Notice(models.Model):
    number = models.CharField(max_length=20, blank=False, null=False, primary_key=True, default=1)
    title = models.CharField(max_length=50, blank=False)
    day = models.DateTimeField(null=False)
    image = models.ImageField(null=True)
    content = models.TextField(max_length=500, blank=False, null=False)
    # Check who is the author of the post - kubs class classifier : class number (which class)
    author = models.CharField(max_length=20, blank=False, default=1, null=False)

    def __str__(self):
        return str(self.title)
