from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class User_detail(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=14)
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField()
    age = models.IntegerField()
    role = models.CharField(max_length=10)
    otp = models.IntegerField(null=True)
    face = models.CharField(max_length=10000,null=True)

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if self.age != None and self.age < 18:
            raise ValidationError(_('Age must be greater than 17'), code='Invalid')

class User_Location(models.Model):
    Locationid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    lattitude =  models.FloatField(max_length=25)
    langitude = models.FloatField(max_length=25)
    userid = models.ForeignKey(User_detail,on_delete=models.CASCADE)
