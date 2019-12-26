from django.shortcuts import render
from django.template.context_processors import csrf
from Auth.models import User_detail
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
import math, random
import datetime
# Create your views here.

class LoginView(TemplateView):
    def get(self, request, **kwargs):
        c = {}
        c.update(csrf(request))
        return render(request, 'Login.html')

    def post(self, request, **kwargs):
        email = request.POST.get('email') 
        password = request.POST.get('pass')
        if(User_detail.objects.filter(email=email,password=password)):
            print("yes")
        else:
            print("no")
        return render(request, 'Login.html')

class RegistrationView(TemplateView):
    def get(self, request, **kwargs):
        c = {}
        c.update(csrf(request))
        return render(request, 'Registration.html',c)
    def post(self, request, **kwargs):
        fullname = request.POST.get('name')
        email = request.POST.get('email') 
        mobile = request.POST.get('mobile')
        age = request.POST.get('age')
        cpass = request.POST.get('confirm-pass')
        password = request.POST.get('pass')
        if password == cpass:
            User_detail.objects.create(name=fullname,email=email,mobile_no=mobile,password=password,age=age,role="user")
        else:
            print("not same")

        return render(request, 'Registration.html')