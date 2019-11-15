from django.contrib import admin
from django.urls import path,include
import main.views

app_name ='main'

urlpatterns = [
    path('',main.views.login,name='login'),
    path('logout',main.views.logout,name='logout'),
    path('home',main.views.home,name='home'),
    path('male_308',main.views.male_308,name='male_308'),
]