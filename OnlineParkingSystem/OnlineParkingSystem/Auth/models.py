from django.db import models

# Create your models here.
class User_detail(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=14)
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField()
    age = models.IntegerField()
    role = models.CharField(default="User",max_length=10)
    otp = models.IntegerField(null=True)
    face = models.CharField(max_length=10000)
