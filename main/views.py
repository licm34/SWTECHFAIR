from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model,login,authenticate
from django.contrib import auth
from main.models import Washer,Dryer
from reserve.models import W_Book,D_Book
from datetime import datetime,timedelta
from django.utils import timezone

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

    Washer_ = Washer.objects.filter(Place='1') # 1 > 308 남자 세탁기만
    
    W_State=[]
    W_Times=[]

    for i in range(0,len(Washer_)):
    
        recent_W = W_Book.objects.filter(MachineId=Washer_[i].id).order_by('-id')[0]
        # Washer[i] > i=0 일때는 1번 세탁기...  / 1번 세탁기 관련 예약을 예약 id 순 내림차순(최근 예약부터)

        if recent_W.EndTime is None: #EndTime 없음.
                W_State.append('사용가능')
                W_Times.append(None)
        
        else: #EndTime 채워져있음
            if recent_W.EndTime <= timezone.now():
                W_State.append('사용가능')
                W_Times.append(None)
            
            else:
                W_State.append('사용중')
                W_Times.append(recent_W.EndTime)

        W_Info = zip(Washer_,W_State,W_Times)

    Dryer_ = Dryer.objects.filter(Place='1') # 1 > 308 남자 세탁기만
    
    D_State=[]
    D_Times=[]

    for i in range(0,len(Dryer_)):
    
        recent_D = D_Book.objects.filter(MachineId=Dryer_[i].id).order_by('-id')[0]
        # Washer[i] > i=0 일때는 1번 세탁기...  / 1번 세탁기 관련 예약을 예약 id 순 내림차순(최근 예약부터)

        if recent_D.EndTime is None: #EndTime 없음.
                D_State.append('사용가능')
                D_Times.append(None)
        
        else: #EndTime 채워져있음
            if recent_D.EndTime <= timezone.now():
                D_State.append('사용가능')
                D_Times.append(None)
            
            else:
                D_State.append('사용중')
                D_Times.append(recent_W.EndTime)

        D_Info = zip(Dryer_,D_State,D_Times)

    return render(request,'main/male_308.html',{
        'W_Info':W_Info,
        'D_Info':D_Info,
    }) 
   
