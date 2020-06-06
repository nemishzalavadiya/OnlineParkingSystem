from django.shortcuts import render
from django.template.context_processors import csrf
from User.models import User_detail
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm,LoginForm,AddLandForm,EditLandForm
from .models import Land_detail,Land_record
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from django.template import loader
import math, random

from User.views import myuser_login_required
# Create your views here.


@myuser_login_required       
def AddLandDetail(request):
    if request.method == 'POST' :
        form = AddLandForm(request.POST,request.FILES)
        if form.is_valid():
            user = User_detail.objects.get(userid=request.POST.get("userid"))
            land = Land_detail()
            land.address= form.cleaned_data["address"]
            land.no_of_spot= form.cleaned_data["no_of_spot"]
            land.description= form.cleaned_data["description"]
            land.city = form.cleaned_data["city"]
            land.end_date = form.cleaned_data["end_date"]
            land.start_date = form.cleaned_data["start_date"]
            land.langitude= form.cleaned_data["langitude"]
            land.lattitude = form.cleaned_data["lattitude"]
            land.verified=form.cleaned_data["verified"]
            land.userid= user
            land.area= form.cleaned_data["area"]
            land.state=form.cleaned_data["state"]
            land.image=form.cleaned_data["image"]
            land.price_per_hour=form.cleaned_data["price_per_hour"]
            land.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'AddLandDetail.html',{'title':'Add Land Detail','message':'Land Registration Failed','form' : form,'login':'True','role':request.session['role']})
    else:
        c = {}
        c.update(csrf(request))
        form = AddLandForm()
        return render(request, 'AddLandDetail.html',{'title':'Add Land Detail','form' : form,'login':'True','role':request.session['role'],'userid':request.session['uid']})

@myuser_login_required
def EditLandDetail(request):
    if request.method == 'POST':
        landid = request.POST.get('landid')
        mydetail = Land_detail.objects.get(landid=landid)
        form = EditLandForm(request.POST,instance=mydetail)
        if form.is_valid():
            form.save()
            user= User_detail.objects.get(email=request.session['email'],role=request.session['role'])
            land=Land_detail.objects.filter(userid_id=user.userid)
            return render(request, 'show.html',{'title':'All Land Detail', 'list' : land,'login':'True','role':request.session['role'],'message':'Edit land detail successfully'})
        else:
            return render(request, 'EditLandDetail.html',{'title':'Edit Land Detail','message':'Edit failed','form' : form,'login':'True','role':request.session['role']})
    else:
        c = {}
        c.update(csrf(request))
        landid = request.GET.get('landid')
        mydetail = Land_detail.objects.get(landid=landid)
        form = EditLandForm(instance=mydetail)
        return render(request, 'EditLandDetail.html',{'title':'Edit Land Detail','form' : form, 'landid' : landid,'login':'True','role':request.session['role']})

@myuser_login_required
def landlist(request):
    userlist= User_detail.objects.get(email=request.session['email'],role=request.session['role'])
    land = Land_detail.objects.filter(userid_id=userlist.userid)
    return render(request, 'show.html',{'title':'All Land Detail', 'list' : land,'login':'True','role':request.session['role'] })
    
@myuser_login_required
def ShowHistory(request):
    landid = request.GET.get("landid")
    landrecords=Land_record.objects.filter(landid=landid)
    landrecords= list(landrecords.values())
    for landrecord in landrecords:
        user = User_detail.objects.get(userid=landrecord['userid_id'])
        landrecord['name']= user.name
        landrecord['email']= user.email
        landrecord['mobile_no']= user.mobile_no
        landrecord['age']= user.age
    return render(request, 'ShowHistory.html',{ 'title':'User History For Land:'+landid,'LandRecord' : landrecords,'login':'True','role':request.session['role'] })

@myuser_login_required
def DeleteLand(request):
    landid = request.GET.get("landid")
    count = Land_record.objects.filter(landid=landid).count()
    user= User_detail.objects.get(email=request.session['email'],role=request.session['role'])
    land=Land_detail.objects.filter(userid_id=user.userid)
    if count==0:
        Land_detail.objects.filter(landid=landid).delete()
        message = "Land deleted successfully!!!"
        return render(request, 'show.html',{ 'title':'All Land Detail','list' : land,'login':'True','role':request.session['role'] ,'message':message})
    else:
        error = "You cann't delete this land because land already reserved by some user!!! sorry for inconvenience"
        return render(request, 'show.html',{ 'title':'All Land Detail','list' : land,'login':'True','role':request.session['role'] ,'error':error})

@myuser_login_required
def Payment(request):
    landid = request.GET.get("landid")
    landrecord = Land_detail.objects.filter(landid=landid)
    landrecord = list(landrecord.values())
    paymentrecords = Land_record.objects.filter(landid=landid,payment_remaining=True)
    count = paymentrecords.count() 
    user = User_detail.objects.get(email=request.session['email'],role=request.session['role'])
    land = Land_detail.objects.filter(userid_id=user.userid)
    if count==0:
        error = "Nothing To Chekout!!"
        return render(request, 'show.html',{'title':'All Land Detail', 'list' : land,'login':'True','role':request.session['role'],'error':error})
    else:
        payment = 24*count*landrecord[0]['price_per_hour']
        paymentrecords.update(payment_remaining=False)
        paymentrecords= list(paymentrecords.values())
        message = "Land payment  successfully done!!!Payment Rs:"+str(payment)
        return render(request, 'show.html',{'title':'All Land Detail', 'list' : land,'login':'True','role':request.session['role'],'message':message})