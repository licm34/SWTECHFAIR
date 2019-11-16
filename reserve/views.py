from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import get_user_model
from main.models import Washer,Dryer
from reserve.models import W_Book,D_Book

def W_reserve(request,id):
    '''User = get_user_model()
    Washer_ = get_object_or_404(Washer,pk=id)

    recent_W = W_Book.objects.filter(MachineId=Washer_.id).order_by('-id')[0]
    recent2_W = W_Book.objects.filter(MachineId=Washer_.id).order_by('-id')[1]

    # 예약 전 정보 보여줄 때 (html render)
    if recent_W.EndTime is None:
        if recent_W.ValidTime <= timezone.now(): # 앞선 사람의 예약 무효 
            case = 1
            time1 = timezone.now() 
            time2 = timezone.now() + timedelta(minutes=10)

        else: # 앞선 사람의 예약 유효
    
    if request.method == 'POST':
        if recent_W.Endtime is None: # 유효한 예약인지 검사해야
            if recent_W.ValidTime <= timezone.now(): # 이 예약은 무효
                # 페널티 부여
                user_p = get_object_or_404(User,pk=recent_W.UserId)
                user_p.Penalty = user_p.Penalty + 1
                user_p.save()

                # 예약 생성
                W_book = W_Book()
                W_book.MachineId = Wahser.pk
                W_book.UserId = User.id
                W_book.ValidTime = timezone.now() + timedelta(minutes=10)
                W_book.save()


        
    '''
    return render(request,'reserve/reserve.html')

def D_reserve(request,id):
    User = get_user_model()
    Dryer_ = get_object_or_404(Dryer,pk=id)

    recent_D = D_Book.objects.filter(MachineId=Dryer_.id).order_by('-id')[0]
    recent2_D = D_Book.objects.filter(MachineId=Dryer_.id).order_by('-id')[1]

    if request.method == 'POST':
        pass
    
    return render(request,'reserve/reserve.html')
