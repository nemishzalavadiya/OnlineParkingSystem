from django.shortcuts import render
from django.template.context_processors import csrf
from Auth.models import User_detail
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from django.template import loader
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
            return render(request,'login.html',{'message':'Login Successful'})
        else:
            print("no")
            return render(request, 'Login.html',{'message':'Invalid email or password!!!'})

def Userdetails(request):
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
    