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
    price_per_hour = models.FloatField()
    start_date  = models.DateField()
    end_date = models.DateField()
    verified = models.BooleanField()
    userid = models.ForeignKey(User_detail,on_delete=models.CASCADE)

class Land_record(models.Model):
    land_record_id = models.AutoField(primary_key=True)
    landid = models.ForeignKey(Land_detail,on_delete=models.CASCADE)
    userid = models.ForeignKey(User_detail,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    start_time=models.TimeField(null=True)
    end_time=models.TimeField(null=True)
    total_price = models.IntegerField()
    payment_remaining = models.BooleanField()
    feedback = models.CharField(null=True,max_length = 255)
    class Meta:
        indexes=[
            models.Index(
                fields=['landid'],name='landid_index'
            ),
            models.Index(
                fields=['userid'],name='userid_index'
            )
        ]