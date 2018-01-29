# -*- coding: utf-8 -*-
from django.db import models
# from multiselectfield import MultiSelectField

# Create your models here.


class Student(models.Model):
    username = models.CharField(max_length=30, blank=False)
    studentid = models.CharField(max_length=10, blank=False)
    password = models.CharField(max_length=40, blank=False)
    email = models.CharField(max_length=50, blank=False)
    #auth =

    FOLLOW_CHOICES = (
        (0, 'UNDERGRADUATE'),
        (1, 'MBA'),
        (2, 'UD_STUDENT_COUNCIL'),
        (3, 'MBA_STUDENT_COUNCIL'),
        (4, 'CLASS_A'),
        (5, 'CLASS_B'),
        (6, 'CLASS_C'),
        (7, 'CLASS_D'),
        (8, 'CLASS_E'),
        (9, 'KUBS_CLUB'),
        (10, 'KUBS_SOCIETY'),
        (11, 'ALUMNI')
    )

    # follow = MultiSelectField(choices=FOLLOW_CHOICES, max_choices=3, default=0, null=False)


class Notice(models.Model):
    number = models.IntegerField(blank=False, null=True)
    title = models.CharField(max_length=50, blank=False)
    day = models.DateTimeField(null=False)
    image = models.ImageField(null=False)
    content = models.TextField(max_length=500, blank=False, null=False)
    auth = models.IntegerField(blank=False, default=1, null=False)