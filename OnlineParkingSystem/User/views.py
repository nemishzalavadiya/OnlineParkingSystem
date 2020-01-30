from django.shortcuts import render
from django.template.context_processors import csrf
from Landlord.models import Land_detail,Land_record
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
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = 'me' #request.META.get('REMOTE_ADDR')
    return ip
    
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
    if request.method == 'POST':
        c = {}
        c.update(csrf(request))
        date = request.POST.get('rdate')
        request.session['date'] = date
        landobj = Land_detail.objects.filter(start_date__lte=datetime.datetime.now(),end_date__gte=datetime.datetime.now(),verified=0)
        lands=list(landobj.values())
        nlands=[]
        for land in lands:
            lat1=land['lattitude']
            lag1=land['langitude']
            g = geocoder.ip(get_client_ip(request))
            lat2,lag2 = g.latlng
            landloc = (lat1,lag1)
            current = (lat2,lag2)
            d=distance.distance(landloc,current).km
            d=round(d, 2)
            land['distance']=d
            count = Land_record.objects.filter(landid=land['landid'],start_date=date).count()
            if land['no_of_spot'] > count:
                nlands.append(land.copy()) 
        print(nlands)
        nlands = list(filter(lambda i: i['distance'] < 10, nlands)) 
        nlands=sorted(nlands, key = lambda i: i['distance'])
        return render(request, 'LandDetails.html',{'Land': nlands,'Date' : date})
    else:
        c = {}
        c.update(csrf(request))
        return render(request, 'LandDetails.html',{'page': 'get'})

def ReserveParking(request):
    c = {}
    c.update(csrf(request))
    landid = request.POST.get('landid')
    userid = 2
    totalprice = float(request.POST.get('price'))
    totalprice = int(totalprice)
    date =  request.session['date']
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    landrecord = Land_record(landid=Land_detail.objects.get(landid=landid),userid=User_detail.objects.get(userid=userid),start_date=date,total_price=totalprice,payment_remaining=True)
    landrecord.save()
    return render(request, 'LandDetails.html',{'message': "successful reserve"})
