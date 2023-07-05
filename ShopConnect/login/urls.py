from django.urls import path
from login import views

urlpatterns=[
    path('',views.home,name=''),
    path('custlogin',views.custlogin,name='custlogin'),
    path('shoplogin',views.shoplogin,name='shoplogin'),
    path('custreg',views.custreg,name='custreg'),
    path('shopreg',views.shopreg,name='shopreg'),
    path('clogin',views.clogin,name='clogin'),
    path('creg',views.creg,name='creg'),
    path('slogin',views.slogin,name='slogin'),
    path('sreg',views.sreg,name='sreg'),
]