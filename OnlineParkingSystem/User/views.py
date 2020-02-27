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
from django.core.mail import send_mail
import geocoder
# Create your views here.
def myuser_login_required(f):
    def login_first(request, *args, **kwargs):
        date='False'
        try:
            if request.POST.get('rdate')!=None:
                date=request.POST.get('rdate')
            if request.session['email']==None:
                c = {}
                c.update(csrf(request))
                form = LoginForm()
                return render(request, 'Login.html',{'message':'Please Login First',"role":'User','form' : form,'date':date})
            else:
                return f(request, *args, **kwargs)
        except:
            c = {}
            c.update(csrf(request))
            form = LoginForm()
            return render(request, 'Login.html',{'message':'Please login,something wrong',"role":'User','form' : form,'date':date})
    login_first.__doc__=f.__doc__
    login_first.__name__=f.__name__
    return login_first

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
        user_data=User_detail.objects.filter(email=email,password=password,role=request.POST.get('role')).first()
        if(user_data):
            request.session['uid']=user_data.userid
            request.session['email']=email
            request.session['role']=request.POST.get('role')
            if request.POST.get('date')!=None:
                return showLand(request,request.POST.get('date'))
            return render(request,'index.html',{'login':'True','role':request.POST.get('role')})
        else:
            return render(request, 'Login.html',{'message':'Invalid email or password!!!','role':request.POST.get('role'),'form' : form})
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
            return render(request, 'Login.html',{'role':request.POST.get('role'),'message':'Registration Successful','form' : form})
        else:
            return render(request, 'Registration.html',{'role':request.POST.get('role'),'message':'Registration Failed','form' : form})
    else:
        c = {}
        c.update(csrf(request))
        form = RegistrationForm()
        return render(request, 'Registration.html',{'form' : form,'role':request.GET.get('role')})

@myuser_login_required    
def EditProfile(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        mydetail = User_detail.objects.get(userid=userid)
        form = EditProfileForm(request.POST,instance=mydetail)
        if form.is_valid():
            form.save()
            return render(request,'index.html',{'login':'True','role':request.session.get('role')})
        else:
            return render(request, 'EditProfile.html',{'login':'True','role':request.session.get('role'),'message':'Edit fail','form' : form})
    else:
        c = {}
        c.update(csrf(request))
        userid = 1
        mydetail = User_detail.objects.get(userid=userid)
        form = EditProfileForm(instance=mydetail)
        return render(request, 'EditProfile.html',{'login':'True','role':request.session.get('role'),'form' : form, 'userid' : userid})

def showLand(request,dateOf):
    if request.method == 'POST':
            c = {}
            c.update(csrf(request))
            date = dateOf
            request.session['date'] = date
            landobj = Land_detail.objects.filter(start_date__lte=date,end_date__gte=date,verified=0)
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
            nlands = list(filter(lambda i: i['distance'] < 100, nlands)) 
            nlands=sorted(nlands, key = lambda i: i['distance'])
            return render(request, 'LandDetails.html',{'login':'True','role':request.session.get('role'),'Land': nlands,'Date' : date})


@myuser_login_required
def ShowLandDetails(request):
    try:
        return showLand(request,request.POST.get('rdate'))
    except:
        c = {}
        c.update(csrf(request))
        form = LoginForm()
        return render(request, 'Login.html',{'message':'Something Went Wrong',"role":'User','form' : form})

def ReserveParking(request):
    c = {}
    c.update(csrf(request))
    landid = request.POST.get('landid')
    userid = request.session['uid']
    totalprice = float(request.POST.get('price'))
    totalprice = int(totalprice)
    date =  request.session['date']
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    landrecord = Land_record(landid=Land_detail.objects.get(landid=landid),userid=User_detail.objects.get(userid=userid),start_date=date,total_price=totalprice,payment_remaining=True)
    landrecord.save()
    land_data = Land_detail.objects.get(landid=landid)
    address=land_data.address
    description=land_data.description
    city=land_data.city
    area=land_data.area
    state=land_data.state
    lattitude=land_data.lattitude
    langitude=land_data.langitude
    subject = 'Confirmation Mail For Booking'
    message = 'Your booking details are below.'+'\n'+'Total price: '+str(totalprice)+'\n'+'Date: '+str(date)+'\n'+'address: '+str(address)+'\n'+'Description: '+str(description)+'\n'+'City: '+str(city)+'\n'+'Area: '+str(area)+'\n'+'State: '+str(state)+'\n'+'Root: '+'http://maps.google.com/?q='+str(lattitude)+','+str(langitude)
    from_email = settings.EMAIL_HOST_USER
    to_list = [request.session['email']]
    send_mail(subject, message, from_email, to_list, fail_silently=False)
    return render(request, 'LandDetails.html',{'login':'True','role':request.session.get('role'),'message': "successful reserve"})

def Home(request):
    loginDone="False"
    try:
        if request.session['email']!=None and request.session['role']!=None:
            loginDone="True"
    except:
        loginDone="False"
        request.session['role']='User'
    return render(request,'index.html',{'login':loginDone,'role':request.session['role']})

@myuser_login_required
def ShowUserHistory(request):
    userid = request.session['uid']
    landrecords = Land_record.objects.filter(userid=userid)
    landrecords= list(landrecords.values())
    for landrecord in landrecords:
        landdetail = Land_detail.objects.get(landid=landrecord['landid_id'])
        user = User_detail.objects.get(userid=landdetail.userid_id)
        landrecord['address']=landdetail.address+","+landdetail.area+","+landdetail.city+","+landdetail.state
        landrecord['name']= user.name
        landrecord['email']= user.email
        landrecord['mobile_no']= user.mobile_no
        landrecord['age']= user.age
    return render(request, 'ShowUserHistory.html',{ 'login':'True','role':request.session.get('role'),'LandRecord' : landrecords })

def LogoutHere(request):
    try:
        del request.session['email']
        del request.session['role']
        loginDone="False"
        return render(request,'index.html',{'login':loginDone,'role':'User'})

    except:
        c = {}
        c.update(csrf(request))
        form = LoginForm()
        return render(request, 'Login.html',{'message':'Please Login First','form' : form})
    
@myuser_login_required
def feedback(request):
    rate = request.GET['rate']
    id = request.GET['id']
    Land_rate_field = Land_record.objects.get(land_record_id=id)
    Land_rate_field.feedback = rate
    Land_rate_field.save()
    return HttpResponseRedirect('../showuserhistory/')