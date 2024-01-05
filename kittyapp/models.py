from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null = False, blank = False, on_delete=models.CASCADE)

    email = models.CharField(max_length=220, blank = False)
    phone_field = models.CharField(max_length=12, blank = False)
    otp = models.CharField(max_length=6)
    image = models.ImageField(upload_to="profile/", max_length=200,blank=True,default="profile/gokussj.png")
    
    def __str__(self):
        return self.user.username
    

class Datastore(models.Model):
    name = models.CharField(max_length=200, blank=False)
    desc = models.TextField(blank=False)
    thumb = models.FileField(upload_to="thumbimage/", blank=True)
    datafile = models.FileField(upload_to="imageandvideo/",max_length=200,null=True,default=None)
   

class Patreon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.CharField(max_length=10,default=0)
    order_id = models.CharField(max_length=200,blank=True)
    razorpayment_id = models.CharField(max_length=200,blank=True)
    paid = models.BooleanField(default=False)


class Improve(models.Model):
    name = models.CharField(max_length=50,blank=False)
    like = models.CharField(max_length=10,blank=False)
    how = models.CharField(max_length=50,blank=False)
    site = models.CharField(max_length=10,blank=False)
    whysite = models.TextField(blank=True)
    def __str__(self):
        return self.name


class Survey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.CharField(max_length=10,blank=False)
    dolike = models.CharField(max_length=50,blank=False)
    site = models.CharField(max_length=10,blank=False)
    improve = models.TextField(blank=False)
    support = models.CharField(max_length=10,blank=False)
    def __str__(self):
        return self.user.username