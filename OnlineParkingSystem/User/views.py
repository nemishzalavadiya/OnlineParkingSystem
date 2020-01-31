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
import math,datetime
from geopy import distance
import geocoder

# Create your views here.
def myuser_login_required(f):
    def login_first(request, *args, **kwargs):
        try:
            if request.session['email']==None:
                c = {}
                c.update(csrf(request))
                form = RegistrationForm()
                return render(request, 'Login.html',{'message':'Please Login First','form' : form})
            else:
                return f(request, *args, **kwargs)
        except:
            c = {}
            c.update(csrf(request))
            form = RegistrationForm()
            return render(request, 'Login.html',{'message':'Please Login First','form' : form})
    login_first.__doc__=f.__doc__
    login_first.__name__=f.__name__
    return login_first

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = form.data['email']
        password = form.data['password']
        if(User_detail.objects.filter(email=email,password=password)):
            request.session['email']=email
            request.session['role']=request.POST.get('role')
            return render(request,'index.html',{'role':request.POST.get('role')})
        else:
            return render(request, 'Login.html',{'message':'Invalid email or password!!!','form' : form})
    else:
        c = {}
        c.update(csrf(request))
        form = LoginForm()
        return render(request, 'Login.html',{'form' : form,'role':request.GET.get('role')})

def Registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = User_detail()
            data.name =form.data['name']
            data.age = form.data['age']
            data.mobile_no = form.data['mobile_no']
            data.password = form.data['password']
            data.email = form.data['email']
            data.role = request.POST['role']
            data.save()
            c = {}
            c.update(csrf(request))
            form = LoginForm()
            return render(request, 'Login.html',{'message':'Registration Successful','form' : form})
        else:
            return render(request, 'Registration.html',{'message':'Registration Failed','form' : form})
    else:
        c = {}
        c.update(csrf(request))
        form = RegistrationForm()
        return render(request, 'Registration.html',{'form' : form,'role':request.GET.get('role')})
    
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
    
@myuser_login_required
def ShowLandDetails(request):
    c = {}
    c.update(csrf(request))
    landobj = Land_detail.objects.filter(start_date__gt=datetime.datetime.now(),verified=0)
    lands=list(landobj.values())
    for land in lands:
        lat1=land['lattitude']
        lag1=land['langitude']
        g = geocoder.ip('me')
        lat2 = g.latlng[0]
        lag2 = g.latlng[1]
        landloc = (lat1,lag1)
        current = (lat2,lag2)
        d=distance.distance(landloc,current).km
        d=round(d, 2)
        land['distance']=d
    lands = list(filter(lambda i: i['distance'] < 10, lands)) 
    lands=sorted(lands, key = lambda i: i['landid'],reverse=True)
    return render(request, 'LandDetails.html',{'Land': lands})

def Home(request):
    loginDone="Fal"
    try:
        if request.session['email']!=None and request.session['role']!=None:
            loginDone="Tr"
    except:
        loginDone="Fal"
    print("value of loginDone is",loginDone,request.session['email'])
    return render(request,'index.html',{'login':loginDone,'role':'User'})

def LogoutHere(request):
    print(request.session['email'],"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",request.session['role'])
    try:
        del request.session['email']
        del request.session['role']
        print("Logout done")
        loginDone="Fal"
        return render(request,'index.html',{'login':loginDone,'role':'User'})

    except:
        c = {}
        c.update(csrf(request))
        form = LoginForm()
        return render(request, 'Login.html',{'message':'Please Login First','form' : form})
