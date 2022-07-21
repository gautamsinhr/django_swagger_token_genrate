# https://stackoverflow.com/questions/31920853/aggregate-and-other-annotated-fields-in-django-rest-framework-serializers
from django.http import response
from rest_framework import serializers
from django.db.models import Sum,Avg,Max,Min,Count
from .models import *


class restorentserializer(serializers.ModelSerializer):
    # username = serializers.SerializerMethodField("get_username")
    class Meta:
        model = Restorent
        fields = ['id','user','restoname','restocity']

        # def get_username(self,b):
        #     username = b.user.username
        #     return username

class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','restoid','catname']


class itemserializer(serializers.ModelSerializer):
    # total_trucks = serializers.IntegerField()
    total_capacity = serializers.IntegerField()
    total_pieces = serializers.SerializerMethodField()
    # total_pieces = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = ['id','restoid','catid','itemname','price','available','total_pieces','total_capacity']
        # fields = '__all__'
    

      
        # def get_total_pieces(self, obj):
        #     totalpieces = Items.objects.all().aggregate(total_pieces=Count('restoid'))
        #     return totalpieces["total_pieces"]
        # def get_total_price(self, obj):
        #     totalprice = Items.objects.all().aggregate(total_price=Sum('price'))
        #     return totalprice["total_price"]


