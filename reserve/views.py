from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import get_user_model
from main.models import Washer,Dryer
from reserve.models import W_Book,D_Book

def W_reserve(request,id):
    User = get_user_model()
    Washer_ = get_object_or_404(Washer,pk=id)

    recent_W = W_Book.objects.filter(MachineId=Washer_.id).order_by('-id')[0]
    recent2_W = W_Book.objects.filter(MachineId=Washer_.id).order_by('-id')[1]

    if request.method == 'POST':
        pass
    
    return render(request,'reserve/reserve.html')

def D_reserve(request,id):
    User = get_user_model()
    Dryer_ = get_object_or_404(Dryer,pk=id)

    recent_D = D_Book.objects.filter(MachineId=Dryer_.id).order_by('-id')[0]
    recent2_D = D_Book.objects.filter(MachineId=Dryer_.id).order_by('-id')[1]

    if request.method == 'POST':
        pass
    
    return render(request,'reserve/reserve.html')
