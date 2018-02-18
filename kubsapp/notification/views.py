# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from notification.models import Student, Notice, Push
from django.http import HttpResponse, JsonResponse
from django.db.models import Max
from pyfcm import FCMNotification


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

def check_password(request):
    if request.method == 'POST':
        received_noti_data = request.body
        received_noti_dict = ast.literal_eval(received_noti_data)

        try:
            received_id = received_noti_dict['studentId']
            received_mail = received_noti_dict['email']
            profile_selected = Student.objects.get(studentid=received_id, email=received_mail)
            sending_pw = profile_selected.password
            return HttpResponse(json.dumps({'response':'success',
                                            'password':sending_pw}))

        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({'response':'fail',
                                            'password':''}))

    else:
        return HttpResponse({'request is not in POST form'})

def post_notice(request):
    if request.method == 'POST':
        received_noti_data = request.body
        received_noti_dict = ast.literal_eval(received_noti_data)

        try:
            fetched_num = (received_noti_dict['number'])

            update_noti = Notice.objects.get(number=fetched_num)
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
    if request.method == 'GET':

        try:
            initial_list = [0,1,2,3,4,5,6,7,8,9,10,11]
            sending_list = []

            for list in initial_list:
                try:
                    sam = Student.objects.get(represent=list)
                    sending_list.append(sam.email)

                except Exception as e:
                    sam = Student.objects.get(represent=100)
                    sending_list.append(sam.email)

            return HttpResponse(json.dumps({'response':'success',
                                            'email':sending_list}))

        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({'response':'fail'}))

    else:
        return HttpResponse(json.dumps({'response':'Request is not in GET form'}))

def send_push(request):

    if request.method == 'POST':

        received_data = request.body
        received_push_dict = ast.literal_eval(received_data)
        push_topic = received_push_dict['topic']
        push_msg = received_push_dict['message']
        push_num = received_push_dict['number']

        try:

            push_service = FCMNotification(api_key='AAAAtoaWwyQ:APA91bFTmtGT2-ku-nnwUgiNgD51IhphQEdemKsAnmfcwVgzwU3OAyxy6UJ8IX7OCZcxWCShPM03_F-IYdfDy6rHs1vbjT04kbngXf7KvGMKUE-cdAFNv4PLEjw2NZMiDE1UU9rxmwcU')

            message_title = "KUB Story"
            message_body = push_msg

            result = push_service.notify_topic_subscribers(topic_name=str(push_topic), message_body=message_body, message_title=message_title)

            sent_push = Push(push_author=push_topic, push_title=push_msg, push_number=push_num)
            sent_push.save()

            return HttpResponse(json.dumps({'response':'success'}))

        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({'response':'fail'}))

    else:
        return HttpResponse('Request is not in POST form')

def push_feed(request, id):

    if request.method == 'GET':

        received_id = id
        selected_user = Student.objects.get(studentid=received_id)
        selected_follow = selected_user.follow
        list_follow = selected_follow.split(',')

        push_list = []
        num = 0

        for list in list_follow:
            if list == 'True':
                push_list.append(num)
                num = num+1
            else:
                num = num+1

        sending_list = []
        for list in push_list:

            sending_dict = {}

            try:
                target = Push.objects.get(push_author=int(list))
                sending_dict['author'] = target.push_author
                sending_dict['title'] = target.push_title
                sending_dict['number'] = target.push_number
                sending_list.append(sending_dict)

            except Exception as e:
                pass

        return HttpResponse(json.dumps({'response': 'success',
                                        'list':sending_list}))
    else:
        return HttpResponse('Request is not in GET form')
