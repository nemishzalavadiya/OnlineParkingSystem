from django.shortcuts import render
from django.template.context_processors import csrf
from User.models import User_detail
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm,LoginForm,AddLandForm
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from django.template import loader
# Create your views here.

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = form.data['email']
        password = form.data['password']
        role = 'Landlord'
        if(User_detail.objects.filter(email=email,password=password,role=role)):
            return render(request,'LandlordLogin.html',{'message':'Login Successful','form' : form})
        else:
            return render(request, 'LandlordLogin.html',{'message':'Invalid email or password!!!','form' : form})
    else:
        c = {}
        c.update(csrf(request))
        form = LoginForm()
        return render(request, 'LandlordLogin.html',{'form' : form})


def Registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.data['role'])
        if form.is_valid():
            form.save()
            return render(request, 'LandlordRegistration.html',{'form' : form})
        else:
            return render(request, 'LandlordRegistration.html',{'message':'Registration Failed','form' : form})
    else:
        c = {}
        c.update(csrf(request))
        form = RegistrationForm()
        return render(request, 'LandlordRegistration.html',{'form' : form})

        
def AddLandDetail(request):
    if request.method == 'POST':
            return render(request, 'AddLandDetail.html',{'message':'Invalid email or password!!!','form' : ''})
    else:
        c = {}
        c.update(csrf(request))
        form = AddLandForm()
        return render(request, 'AddLandDetail.html',{'form' : form})

    