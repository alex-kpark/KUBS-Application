# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from Users.models import User
import json
from django.http import JsonResponse, HttpResponse

def yes():
    user_inst = User(username='name', email='mailinfo')
    user_inst.save()
    return 'yes'

def user_login(request):
    if request.method == 'POST':
        try:
            userid = User.objects.get(studentid=request.post['studentId'], password=request.post['password'])
            ran_list = Notice.objects.filter(day=request.post['day'])
            return HttpResponse(json.dumps({'response':'success',
                                            'monthly_schedule' : ran_list}))

            # return JsonResponse(json.dumps({'response':'success',
            #                                 'monthly_schedule': ran_list}))

        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({'response':'fail'}))


        serializer = UserSerializer(userinfo, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializer, status=status.HTTP_400_BAD_REQUEST)