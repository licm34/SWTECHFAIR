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

def myinfo_edit(request):
    User = get_user_model()
    if request.method == 'POST':
        user = get_object_or_404(User,UserName=request.user.UserName)
        if request.POST['PassWord'] == request.POST['Confirm']:
            PassWord = request.POST['PassWord']
            user.set_password(PassWord)
            user.CardId = request.POST['CardId']
            user.save()
            auth.login(request,user)
            return redirect('/account/myinfo')  # 성공 > myinfo
        else:
            return render(request,'account/myinfo_edit.html',{'fail':True}) 
            # 실패 > 다시 내 정보, 팝업 뜨게. 확인해봐야
    return render(request,'account/myinfo_edit.html')