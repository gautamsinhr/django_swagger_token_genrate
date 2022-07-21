from django.urls import path,include
from django.db import router
from  django.urls import path
from .import views
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
from app.models import *
from app.views import *


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="demo swagger API",
      default_version='v1',
      # description="Test description",
      # terms_of_service="https://www.google.com/policies/terms/",
      # contact=openapi.Contact(email="contact@xyz.local"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router.register('restoapi',restoapi,basename='restoapi')
router.register('categoryapi',categoryapi,basename='categoryapi')
router.register('itemapi',itemapi,basename='itemapi')
router.register('restobyid',restobyid,basename='restobyid')
router.register('itembyrestorent',itembyrestorent,basename='itembyrestorent')
router.register('pricegrater50',pricegrater50,basename='pricegrater50')
router.register('restoinitem',restoinitem,basename='restoinitem')

urlpatterns = [

    path('admin/',admin.site.urls),
    # path('itemapi/',views.itemapi,name='itemapi'),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),     ## for login biltin provide ui  
    path('gettoken/',obtain_auth_token), ## for genrating token
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('',include(router.urls)),
     
   
    # path('itemapi',restoapi.as_view(),name='restoapi'),
  
]
