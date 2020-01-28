from django.shortcuts import render
from django.template.context_processors import csrf
from Landlord.models import Land_detail
from django.views.generic import TemplateView,ListView
from .models import User_detail
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm,LoginForm,EditProfileForm
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from django.template import loader
import math
# Create your views here.

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = form.data['email']
        password = form.data['password']
        role = 'User'
        if(User_detail.objects.filter(email=email,password=password,role=role)):
            return render(request,'Login.html',{'message':'Login Successful','form' : form})
        else:
            return render(request, 'Login.html',{'message':'Invalid email or password!!!','form' : form})
    else:
        c = {}
        c.update(csrf(request))
        form = LoginForm()
        return render(request, 'Login.html',{'form' : form})

def Registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Registration.html',{'form' : form})
        else:
            return render(request, 'Registration.html',{'message':'Registration Failed','form' : form})
    else:
        c = {}
        c.update(csrf(request))
        form = RegistrationForm()
        return render(request, 'Registration.html',{'form' : form})
    
def EditProfile(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        mydetail = User_detail.objects.get(userid=userid)
        form = EditProfileForm(request.POST,instance=mydetail)
        if form.is_valid():
            form.save()
            return render(request, 'EditProfile.html',{'form' : form})
        else:
            return render(request, 'EditProfile.html',{'message':'Edit fail','form' : form})
    else:
        c = {}
        c.update(csrf(request))
        userid = 1
        mydetail = User_detail.objects.get(userid=userid)
        form = EditProfileForm(instance=mydetail)
        return render(request, 'EditProfile.html',{'form' : form, 'userid' : userid})
    
def ShowLandDetails(request):
    c = {}
    c.update(csrf(request))
    landobj = Land_detail.objects.filter(verified=0)
    lands=list(landobj.values())
    for land in lands:
        R = 6371
        lat1=land['lattitude']
        lag1=land['langitude']
        lat2 = 21.8002
        dLat = (21.8002-lat1) * math.pi / 180
        dLon = (72.9565-lag1) * math.pi / 180
        a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(lat1 * math.pi / 180 ) * math.cos(lat2 * math.pi / 180 ) * math.sin(dLon/2) * math.sin(dLon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R * c-land['landid']
        land['d']=d
    lands=sorted(lands, key = lambda i: i['landid'],reverse=True)
    print(lands)
    return render(request, 'LandDetails.html',{'Land': lands})
