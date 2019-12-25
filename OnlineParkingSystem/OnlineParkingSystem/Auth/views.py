from django.shortcuts import render
from django.template.context_processors import csrf
from Auth.models import User_detail
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
import math, random
import datetime
# Create your views here.


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,"login.html",c)


def registration(request):
    c = {}
    c.update(csrf(request))
    return render(request,"registration.html",c)