from django.forms import ModelForm , Textarea
from django import forms
from .models import User_detail
import re 
class RegistrationForm(ModelForm):
    class Meta:
        model=User_detail
        fields=('name','password','mobile_no','email','age','role')
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
            }),
            'role': forms.HiddenInput(attrs={
                "id":"role",
            }),
        }
    def clean(self):
        cleaned_data = super().clean()
        self.errors.clear()
        mobile_no = cleaned_data.get("mobile_no")
        age = cleaned_data.get("age")
        password = cleaned_data.get("password")
        if re.match("[6-9][0-9]{9}",mobile_no) == None:
            msg = "Mobile Number must be valid."
            self.add_error('mobile_no', msg)
        if age == None or int(age) <18 :
            msg = "Age must grater than or equal to 18"
            self.add_error('age', msg)
        if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}',password) == None:
            msg = "Password must be valid(length is atleast 8)."
            self.add_error('password', msg)

class LoginForm(ModelForm):
    class Meta:
        model=User_detail
        fields=('email','password')
        widgets = {
            'password': forms.PasswordInput(attrs={
                "class":"input100",
                "id":"password",
                "placeholder":"Password"
            }),
            'email': forms.EmailInput(attrs={
                "class":"input100",
                "id":"email",
                "placeholder":"Email Address"
            })
        }

class EditProfileForm(ModelForm):
    class Meta:
        model=User_detail
        fields=('userid','name','mobile_no','email','age')
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
            'email': forms.EmailInput(attrs={
                "class":"input100",
                "id":"email",
                "placeholder":"Email Address..."
            }),
            'userid': forms.TextInput(attrs={
                "id":"userid"
            }),
        }
    def clean(self):
        cleaned_data = super().clean()
        self.errors.clear()
        mobile_no = cleaned_data.get("mobile_no")
        age = cleaned_data.get("age")
        if re.match("[6-9][0-9]{9}",mobile_no) == None:
            msg = "Mobile Number must be valid."
            self.add_error('mobile_no', msg)
        if age == None or int(age) <18 :
            msg = "Age must be valid."
            self.add_error('age', msg)