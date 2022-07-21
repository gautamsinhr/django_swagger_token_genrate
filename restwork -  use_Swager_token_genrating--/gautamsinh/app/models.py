from typing_extensions import NotRequired
from django.db import models
from  django.contrib.auth.models import User
from numpy import require
# Create your models here.


class Restorent(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    restoname  = models.CharField(max_length=10)
    restocity  = models.CharField(max_length=10)

    def __str__(self):
        return  self.restoname


class Category(models.Model):
    restoid = models.ForeignKey(Restorent,on_delete=models.CASCADE)
    catname = models.CharField(max_length=10)

    def __str__(self):
        return  self.catname
    
class Items(models.Model):
    restoid = models.ForeignKey(Restorent,on_delete=models.CASCADE)
    catid = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='cat')
    itemname = models.CharField(max_length=10,null=True,blank=True)
    # itemsdtaa = models.CharField(max_length=10,null=True)
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)    


    def __str__(self):
        return  self.restoid.restoname



   