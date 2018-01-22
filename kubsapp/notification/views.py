# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from notification.models import Student, Notice
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.

def student_login(request):
    if request.method == 'POST':
        try:
            student_id = Student.objects.get(studentid=request.POST['studentId'], password=request.POST['password'])
            return HttpResponse(json.dumps({'response':'success'}))

        except Exception as e:
            return HttpResponse(json.dumps({'response':'fail'}))

def check_studentid(request):
    pass

def sign_up(request):
    pass

def set_follow(request):
    pass

def check_follow(request):
    pass

def check_profile(request):
    pass

def post_notice(request):
    pass

def post_monthly_schedule(request):
    pass

def post_daily_schedule(request):
    pass

def get_specific_event(request):
    pass

