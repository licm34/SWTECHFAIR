from django.contrib import admin
from django.urls import path,include
import reserve.views

app_name='reserve'

urlpatterns = [
    path('W_reserve/<int:id>',reserve.views.W_reserve,name='W_reserve'),
    path('D_reserve/<int:id>',reserve.views.D_reserve,name='D_reserve'),
]