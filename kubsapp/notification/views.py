# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from notification.models import Student, Notice
from django.http import HttpResponse, JsonResponse
from django.db.models import Max

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

#Does it need to be done?
def check_studentid(request):
    return HttpResponse({'response':'not developed'})

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

    if request.method == 'POST':
        received_setfollow_data = request.body
        setfollow_data_dict = ast.literal_eval(received_setfollow_data)

        try:
            target=Student.objects.get(studentid=setfollow_data_dict['studentId'])
            target.follow = setfollow_data_dict['follow']
            target.save()
            return HttpResponse(json.dumps({'response':'success'}))

        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({'response':'fail'}))

    else:
        return HttpResponse({'response':'Request is not in POST'})

def get_follow(request, studentId):

    if request.method == 'GET':
        # received_checkfollow_data = request.body
        # checkfollow_data_dict = ast.literal_eval(received_checkfollow_data)

        try:
            received_id_data = studentId
            selected_user = Student.objects.get(studentid=received_id_data)
            selected_follow = selected_user.follow
            return HttpResponse(json.dumps({'response':'success',
                                            'follow':selected_follow}))

        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({'response':'fail'}))

    else:
        return HttpResponse(json.dumps({'response':'Request is not in GET'}))

#Auth needs to be added
def check_profile(request, studentId):
    if request.method == 'GET':
        try:
            received_id_data = studentId
            profile_selected = Student.objects.get(studentid=received_id_data)
            profile_name = profile_selected.username
            profile_repre = profile_selected.represent
            return HttpResponse(json.dumps({'response':'success',
                                            'name':profile_name,
                                            'represent':profile_repre}))
        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({'response':'fail'}))

    else:
        return HttpResponse({'response':'Request is not in GET'})


def post_notice(request):
    if request.method == 'POST':
        received_noti_data = request.body
        received_noti_dict = ast.literal_eval(received_noti_data)

        try:
            fetched_num = (received_noti_dict['number'])

            update_noti = Notice.objects.get(number=fetched_num)


            #Day not fixed

            update_noti.day = received_noti_dict['day']
            update_noti.author = received_noti_dict['auth']
            update_noti.title = received_noti_dict['title']
            update_noti.content = received_noti_dict['content']
            update_noti.image = received_noti_dict['image']

            update_noti.save()
            return HttpResponse(json.dumps({'response':'success'}))

        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({'response':'fail'}))

    else:
        return HttpResponse({'request is not in POST form'})


def number_increase(request, auth):
    if request.method == 'POST':

        received_data = request.body
        received_dict = ast.literal_eval(received_data)
        received_auth = int(received_dict['auth'])

        if (0<=received_auth<12 or received_auth==100):
            try:

                temp_Notice = Notice.objects.all()
                # print(temp_Notice)

                num = temp_Notice[len(temp_Notice)-1]
                max_num = int(num.number)
                # print(type(max_num))
                sending_num = max_num+1
                # print(sending_num)
                new_info = Notice(number=sending_num)
                # print(new_info)
                new_info.save()

                return HttpResponse(json.dumps({'response':'success',
                                                'increased':sending_num}))
            except Exception as e:
                print(str(e))
                return HttpResponse(json.dumps({'response':'fail'}))

        else:
            print('author is not approved')
            return HttpResponse('Approval denied')
    else:
        return HttpResponse({'request is not in POST form'})


def delete_post(request, auth):
    if request.method == 'POST':

        received_data = request.body
        received_dict = ast.literal_eval(received_data)
        received_num = int(received_dict['number'])

        try:
            target = Notice.objects.get(number=received_num)
            target.delete()
            return HttpResponse(json.dumps({'response':'success'}))

        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({'response':'fail'}))

    else:
        return HttpResponse({'request is not in POST form'})


def get_monthly_schedule(request, year, month, id):

    if request.method == 'GET':
        try:

            request_student = Student.objects.get(studentid=id)
            follow_info = request_student.follow
            info = follow_info.split(',')
            list = []
            number = -1
            for i in info:
                number += 1
                if i == 'True':
                    list.append(number)
            results = Notice.objects.filter(author__in=list)

            sending_list=[]
            for result in results:
                input = str(result.day)[0:7]
                input_month = input[5:7]
                if input_month == month:
                    sending_list.append(str(result.day))
                # print(sending_list)
            return HttpResponse(json.dumps({'response':'success',
                                            'list':sending_list}))

        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({'response':'fail'}))

    else:
        return HttpResponse(json.dumps({'response':'Request is not in GET form'}))


def get_daily_schedule(request, year, month, day, id):

    if request.method == 'GET':
        try:
            request_student = Student.objects.get(studentid=id)
            follow_info = request_student.follow
            info = follow_info.split(',')
            list = []
            number = -1
            for i in info:
                number += 1
                if i == 'True':
                    list.append(number)
            results = Notice.objects.filter(author__in=list)
            # print(list)

            sending_list = []
            for result in results:
                input = str(result.day)[0:11]
                input_month = str(result.day)[5:7]
                input_day = str(result.day)[8:10]

                # print("test"+input_month+"!")
                # print("test"+month+"!")

                if str(input_day) == str(day):
                    if str(input_month) == str(month):
                        dict = {'number':result.number, 'title':result.title , 'author':str(result.author), 'day':str(result.day)}
                        sending_list.append(dict)

                else:
                    pass

            return HttpResponse(json.dumps({'response':'success',
                                            'daily':sending_list}))

        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({'response':'fail'}))

    else:
        return HttpResponse(json.dumps({'response':'Request is not in GET form'}))


def get_specific_event(request, num):
    pass

    if request.method == 'GET':

        try:
            selected_notice = Notice.objects.get(number=num)
            sending_number = selected_notice.number
            sending_author = selected_notice.author
            sending_day = str(selected_notice.day)
            sending_title = selected_notice.title
            sending_content = selected_notice.content
            sending_image = str(selected_notice.image)

            return HttpResponse(json.dumps({'response':'success',
                                            'no':sending_number,
                                            'author':sending_author,
                                            'day':sending_day,
                                            'title':sending_title,
                                            'content':sending_content,
                                            'image':sending_image}))

        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({'response':'fail'}))

    else:
        return HttpResponse(json.dumps({'response':'Request is not in GET form'}))


def check_email(request):
    pass
    # if request.method == 'GET':
    #     try:
    #         email_0 = Student.objects.get(represent='0').email
    #         email_1 = Student.objects.get(represent='1').email
    #         email_2 = Student.objects.get(represent='2').email
    #         # email_3 = Student.objects.get(represent='3').email
    #         # email_4 = Student.objects.get(represent='4').email
    #         # email_5 = Student.objects.get(represent='5').email
    #         # email_6 = Student.objects.get(represent='6').email
    #         # email_7 = Student.objects.get(represent='7').email
    #         # email_8 = Student.objects.get(represent='8').email
    #         # email_9 = Student.objects.get(represent='9').email
    #         # email_10 = Student.objects.get(represent='10').email
    #         # email_11 = Student.objects.get(represent='11').email
    #
    #         return HttpResponse(json.dumps({'0':email_0,
    #                                         '1':email_1,
    #                                         '2': email_2}))
    #                                         # '3': email_3,
    #                                         # '4': email_4,
    #                                         # '5': email_5,
    #                                         # '6': email_6,
    #                                         # '7': email_7,
    #                                         # '8': email_8,
    #                                         # '9': email_9,
    #                                         # '10': email_10,
    #                                         # '11': email_11}))
    #
    #     except Exception as e:
    #         print(str(e))
    #         return HttpResponse(json.dumps({'response':'fail'}))
    #
    # else:
    #     return HttpResponse(json.dumps({'response':'Request is not in GET form'}))