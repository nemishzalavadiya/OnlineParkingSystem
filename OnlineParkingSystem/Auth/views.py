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
        return render(request, 'Login.html',c)

class RegistrationView(TemplateView):
    def get(self, request, **kwargs):
        c = {}
        c.update(csrf(request))
        return render(request, 'Registration.html',c)