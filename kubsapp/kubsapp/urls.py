"""kubsapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from notification.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #login(POST)
    url(r'^login/$', student_login),

    #check studentid(GET)
    url(r'^check_studentid/$', check_studentid),

    #sign up(POST)
    url(r'^signup/$', sign_up),

    #set_follow (POST)
    url(r'^follow/$', set_follow),

    #check_follow
    url(r'^get_follow/([0-9]{10})/$', get_follow),

    #check_profile
    url(r'^check_profile/([0-9]{10})/$', check_profile),

    #check_password
    url(r'^check_password/$', check_password),

    #post_notice
    url(r'^post_notice/$', post_notice),

    #increase the number
    url(r'^post/([0-9]+)/$', number_increase),

    #delete notice with given number
    url(r'delete_post/([0-9]+)/$', delete_post),

    #get_monthly_schedule
    url(r'^monthly_schedule/([0-9]{4})-([0-9]{2})/([0-9]{10})/$', get_monthly_schedule),

    #get_daily_schedule
    url(r'^daily_schedule/([0-9]{4})-([0-9]{2})-([0-9]{2})/([0-9]{10})/$', get_daily_schedule),

    #get_specific_event
    url(r'^event/([0-9]+)/$', get_specific_event),

    #send_email
    url(r'^email/$', check_email),

    #push
    url(r'^push/$', send_push),

    #push_feed
    url(r'^feed/([0-9]{10})/$', push_feed),
]
