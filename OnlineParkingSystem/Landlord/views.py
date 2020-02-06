from django.shortcuts import render
from django.template.context_processors import csrf
from User.models import User_detail
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm,LoginForm,AddLandForm
from .models import Land_detail,Land_record
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from django.template import loader
from User.views import myuser_login_required
# Create your views here.


@myuser_login_required       
def AddLandDetail(request):
    if request.method == 'POST' :
        form = AddLandForm(request.POST,request.FILES)
        if form.is_valid():
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
            land.userid= form.cleaned_data["userid"]
            land.area= form.cleaned_data["area"]
            land.state=form.cleaned_data["state"]
            land.image=form.cleaned_data["image"]
            land.price_per_hour=form.cleaned_data["price_per_hour"]
            land.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'AddLandDetail.html',{'message':'Registration2 Failed','form' : form})
    else:
        c = {}
        c.update(csrf(request))
        form = AddLandForm()
        return render(request, 'AddLandDetail.html',{'form' : form})
@myuser_login_required
def EditLandDetail(request):
    if request.method == 'POST':
        landid = request.POST.get('landid')
        mydetail = Land_detail.objects.get(landid=landid)
        form = AddLandForm(request.POST,instance=mydetail)
        if form.is_valid():
            form.save()
            return render(request, 'EditLandDetail.html',{'form' : form})
        else:
            return render(request, 'EditLandDetail.html',{'message':'Edit fail','form' : form})
    else:
        c = {}
        c.update(csrf(request))
        landid = 1
        mydetail = Land_detail.objects.get(landid=landid)
        form = AddLandForm(instance=mydetail)
        return render(request, 'EditLandDetail.html',{'form' : form, 'landid' : landid})

@myuser_login_required
def landlist(request):
    userlist= User_detail.objects.get(email=request.session['email'],role=request.session['role'])
    land=Land_detail.objects.filter(userid_id=userlist.userid)
    return render(request, 'show.html',{ 'list' : land })
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
    return render(request, 'ShowHistory.html',{ 'LandRecord' : landrecords })
