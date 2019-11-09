from django.contrib import admin
from django.urls import path,include
import account.views

app_name ='account'

urlpatterns = [
    path('signup',account.views.signup,name='signup'),
    path('myinfo',account.views.myinfo,name='myinfo'),
    #path('myinfo/edit/<str:UserName>',account.views.myinfo_edit,name='myinfo_edit'),
]