from django import forms
from Auth.models import User_detail


class User_detailForm(forms.ModelForm):
    class Meta:
        model=User_detail
        fields=('name','password','mobile_no','email','age',)