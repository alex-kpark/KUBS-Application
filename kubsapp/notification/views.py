# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from notification.models import Student, Notice
from django.http import HttpResponse, JsonResponse

from django.shortcuts   import render
import json
import ast

# Create your views here.

def student_login(request):

    if request.method == 'POST':
        received_login_data = request.body #in str form
        login_data_dict = ast.literal_eval(received_login_data) #change into dict

        try:
            result = Student.objects.get(studentid=login_data_dict['studentId'], password=login_data_dict['password'])
            return HttpResponse(json.dumps({'response':'success'}, ensure_ascii=False))

        except Exception as e:
            print (str(e))
            return HttpResponse(json.dumps({'response':'fail'}, ensure_ascii=False))
    else:
        pass

def check_studentid(request):
    return HttpResponse({'response':'exitsignu'})
    # if request.method == 'GET':
    #     received_id_data = request.body
    #     checkid_data_dict = ast.literal_eval(received_id_data)
    #     print(check_data_dict)
    #
    #     # try:
    #     #     result =

def sign_up(request):

    if request.method == 'POST':
        received_signup_data = request.body
        signup_data_dict = ast.literal_eval(received_signup_data)
        # print(type(signup_data_dict))
        # print(signup_data_dict)

        try:
            #To bring the table, just open the smallest bracket and put params
            new_signed_info = Student(username=signup_data_dict['name'],
                          studentid=signup_data_dict['studentId'],
                          password=signup_data_dict['password'],
                          email=signup_data_dict['email'])
            new_signed_info.save()
            return HttpResponse(json.dumps({'response':'success'}))

        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({'response':'fail'}))

    else:
        return HttpResponse({'response':'Request is not in POST'})


def set_follow(request):
    pass
    # if request.method == 'POST':
    #     received_follow_data = request.body
    #     follow_data_dict = ast.literal_eval(received_follow_data)
    #
    # try:
    #
    #
    #
    #
    #
    # except Exception as e:
    #     print(str(e))
    #     return HttpResponse(json.dumps({'response':'fail'}))

def check_follow(request):
    pass

#EOF Error..?
def check_profile(request):
    pass
    # if request.method == 'GET':
    #     requested_profile_data = request.body
    #     requested_profile_dict = ast.literal_eval(requested_profile_data)
    #     print(requested_profile_dict)
    #
    #     try:
    #         student_profile = Student.objects.get(studentid=requested_profile_dict['studentId'])
    #         print(student_profile)
    #         print(type(student_profile))
    #         return HttpResponse(json.dumps({'response':'success'}))
    #
    #     except Exception as e:
    #         print(str(e))
    #         return HttpResponse(json.dumps({'response':'fail'}))
    #
    # else:
    #     return HttpResponse({'response':'Request is not in GET'})

def post_notice(request):
    if request.method == 'POST':
        received_noti_data = request.body
        received_noti_dict = ast.literal_eval(received_noti_data)

        #number is necessary to be added - auto increase
        #null is currently approved temporary way
        try:
            new_noti = Notice(auth=received_noti_dict['auth'],
                              day=received_noti_dict['day'],
                              title=received_noti_dict['title'],
                              content=received_noti_dict['content'],
                              image=received_noti_dict['image']
                              )
            new_noti.save()
            return HttpResponse(json.dumps({'response':'success'}))

        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({'response':'fail'}))

    else:
        HttpResponse({'request is not in POST form'})

def post_monthly_schedule(request):
    pass

def post_daily_schedule(request):
    pass

def get_specific_event(request):
    pass