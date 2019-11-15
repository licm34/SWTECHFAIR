from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model,login,authenticate
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        UserName = request.POST['UserName']
        password = request.POST['PassWord']
        user = auth.authenticate(request,UserName=UserName, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            return redirect('/')
    return render(request,'main/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    return render(request,'main/home.html')

def male_308(request):
    return render(request,'main/male_308.html')


