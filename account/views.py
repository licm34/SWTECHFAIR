from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model,login,authenticate
from django.contrib import auth

# Create your views here.
def signup(request):
    User = get_user_model()
    if request.method == 'POST':
        if request.POST['PassWord'] == request.POST['Confirm']:
            user = User.objects.create_user(
                UserName=request.POST['UserName'],
                CardId=request.POST['CardId'],
                password = request.POST['PassWord']
            )
            auth.login(request,user)
            return redirect('/home')
    return render(request,'account/signup.html') #signup 페이지 렌더링

def myinfo(request):
    return render(request,'account/myinfo.html')