#  Token fc4a46f35425481d8ca11c1fc7fd05e78ce72eb5


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Sum,Avg,Max,Min,Count
from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework import viewsets
from .models import *    
## SEARCH FILTER ##
from rest_framework.response import Response
from rest_framework.filters import  SearchFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


def home(request):
    return render(request,'app/home.html')

class restoapi(viewsets.ModelViewSet):
    serializer_class = restorentserializer
    queryset = Restorent.objects.all()
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
   


    # def get_queryset(self):
    #    data = Restorent.objects.get()






class categoryapi(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = categoryserializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
   


class itemapi(viewsets.ModelViewSet):
    queryset = Items.objects.all().order_by('price')
    serializer_class = itemserializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['itemname','available','price']



# restorent and this item count 
class restobyid(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    
    def retrieve(self,request,*args,**kwargs):
        params = kwargs
        # a = Restorent.objects.get('restoname')
     
        print(params['pk'])  
        queryset = Items.objects.filter(restoid=params['pk'])
        p = queryset.count()
        print(p)
        serializer= itemserializer(queryset,many=True)
        return Response([serializer.data, 'This is totle item ',p])
       
 

        

#  restorent by items 
class itembyrestorent(viewsets.ModelViewSet):
    serializer_class = itemserializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
   
    def retrieve(self,**kwargs):
        params = kwargs
        print(params['pk'])  ###
        queryset = Items.objects.filter(restoid=params['pk'])
        print(queryset,'------')
        serializer= itemserializer(queryset,many=True)
        print(serializer)
        return HttpResponse(serializer.data)     
#    
class itembyrestorent(viewsets.ModelViewSet):
    
    http_method_names = ['get']
   
    def retrieve(self,request,*args,**kwargs):
        params = kwargs
        print(params['pk'])  ###
        itemsdata = Items.objects.filter(restoid=params['pk'])
        serializer = itemserializer(itemsdata,many=True)

        return  Response(serializer.data)   


# if item in  in restorent then show  restorent  detailes
class restoinitem(viewsets.ModelViewSet):
    serializer_class = itemserializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    
    def get_queryset(self):
        queryset = Items.objects.exclude(itemname="")

        # print(queryset,'------------')
        return queryset



#  grater item price 50


class pricegrater50(viewsets.ModelViewSet):
# class pricegrater50(GenericAPIView):
    http_method_names = ['get']
    # serializer_class = restorentserializer
    serializer_class = itemserializer
    queryset = Items.objects.all()
    
    def get_queryset(self):
        resto_data = Restorent.objects.all()
        totalresto = []
        for i in resto_data:
            itemobj = Items.objects.filter(restoid=i.id)
            a  = itemobj.aggregate(tprice=Sum('price'))
            if a['tprice'] is not None:
                if a['tprice']>500:
                    totalresto.append(i)
                else:
                    pass 
            else:  
                pass       
        print(totalresto,'---')
        return Items.objects.annotate(
            total_pieces=Count('restoid'),
            total_capacity=Sum('price'),
            
            
   
        )
   
    # def checkdata(self):    
    #     # queryset = Items.objects.aggregate(price=Max('price'))
    #     # queryset =  Items.objects.annotate(num_votes=Max('price')).filter(price__gt=500)
    #     resto_data = Restorent.objects.all()
    #     totalresto = []
    #     for i in resto_data:
    #         itemobj = Items.objects.filter(restoid=i.id)
    #         a  = itemobj.aggregate(tprice=Sum('price'))
    #         if a['tprice'] is not None:
    #             if a['tprice']>500:
    #                totalresto.append(i)
    #             else:
    #                 pass 
    #         else:  
    #             pass        
   
    #     p = (totalresto)
    #     print (p)

    #     serializer = itemserializer(resto_data,many=True)
    #     return  Response(serializer.data)   ##  Response(serializer.data)
      





    
    # def get_queryset(self):
    #     return Items.objects.filter(
    #      restoid__in=Restorent.objects.annotate(Sum('price')))\
    #         .filter(price__gt=0)

    # def get_queryset(self):
        # queryset = super().get_queryset()
        # a = Restorent.objects.all()
        # c = []
        # for i in a:
        #     queryset = Items.objects.filter(restoid=i.id).aggregate(totleprice = Sum('price'))
        #     if queryset['totleprice']>500:
        #         c.append(i)
        #         print(c,'nnjkj')
        #         return c
                
        # print(c)
        # return  ({})
          
        # serializer = itemserializer(c,many=True)
        # return  queryset
        