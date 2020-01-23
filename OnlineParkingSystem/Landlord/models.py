from django.db import models
from User.models import User_detail
# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Land_detail(models.Model):
    landid = models.AutoField(primary_key=True)
    lattitude =  models.FloatField(max_length=25)
    langitude = models.FloatField(max_length=25)
    address = models.CharField(max_length=255)
    image = models.ImageField(null=True,upload_to='images/%Y/%m/%d')
    city = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    state = models.CharField(max_length=255) 
    no_of_spot = models.IntegerField()
    description = models.TextField(null=True)
    availability = models.IntegerField()
    price_per_hour = models.FloatField()
    start_date  = models.DateField()
    end_date = models.DateField()
    verified = models.BooleanField()
    userid = models.ForeignKey(User_detail,on_delete=models.CASCADE)
