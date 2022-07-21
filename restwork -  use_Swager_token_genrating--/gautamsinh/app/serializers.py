from django.http import response
from rest_framework import serializers
from django.db.models import Sum,Avg,Max,Min,Count
from .models import *


class restorentserializer(serializers.ModelSerializer):
    class Meta:
        model = Restorent
        fields = ['id','user','restoname','restocity']



class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','restoid','catname']


class itemserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Items
        # fields = ['id','restoid','catid','itemname','price','available']
        fields = '__all__'
    

        
        
        # def get_total_pieces(self, obj):
        #     totalpieces = Restorent.objects.all().aggregate(total_restorent=Count('id'))
        #     return totalpieces["total_pieces"]
        # def get_total_price(self, obj):
        #     totalprice = Items.objects.all().aggregate(price=Sum('price'))
        #     return totalprice["total_price"]


