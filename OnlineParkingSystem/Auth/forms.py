from django.forms import ModelForm , Textarea
from django import forms
from Auth.models import User_detail


class RegistrationForm(ModelForm):
    class Meta:
        model=User_detail
        fields=('name','password','mobile_no','email','age')
        widgets = {
            'age': forms.NumberInput(attrs={
                "class":"input100",
                "id":"age",
                "placeholder":"Age"
            }),
            'name': forms.TextInput(attrs={
                "class":"input100",
                "id":"name",
                "placeholder":"Name"
            }),
            'mobile_no': forms.NumberInput(attrs={
                "class":"input100",
                "id":"mobile_no",
                "placeholder":"Mobile Number"
            }),
            'password': forms.PasswordInput(attrs={
                "class":"input100",
                "id":"password",
                "placeholder":"*********"
            }),
            'email': forms.EmailInput(attrs={
                "class":"input100",
                "id":"email",
                "placeholder":"Email Address..."
            })
        }
        

class LoginForm(ModelForm):
    class Meta:
        model=User_detail
        fields=('name','password','role')