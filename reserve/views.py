from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import get_user_model
from main.models import Washer,Dryer
from reserve.models import W_Book,D_Book
from datetime import datetime,timedelta
from django.utils import timezone

def W_reserve(request,id):
    User = get_user_model()
    User_ = request.user
    Washer_ = get_object_or_404(Washer,pk=id)

    # 모델에 기본 데이터 넣어줘야
    recent_W = W_Book.objects.filter(MachineId=Washer_.id).order_by('-id')[0]

    # 예약 전 정보 보여줄 때 (html render)
    if recent_W.EndTime is None:
        if recent_W.ValidTime <= timezone.now():
            if request.method == 'POST':
                user_p = get_object_or_404(User,UserName=recent_W.UserId)
                user_p.Penalty = user_p.Penalty + 1
                user_p.save()

                # 예약 생성
                W_book = W_Book()
                W_book.MachineId = Washer_.Number
                W_book.UserId = User_.UserName
                W_book.ValidTime = timezone.now() + timedelta(minutes=10)
                W_book.save()
                return redirect('/male_308') # 고치기
            
            else:
                case = 1
                error = False
                time1 = timezone.now() 
                time2 = timezone.now() + timedelta(minutes=10) # 현재 이용자 예약 진행해줘야
                return render(request,'reserve/reserve.html',{
                    'Washer':Washer_,
                    'error':error,
                    'time1':time1,
                    'time2':time2,
                })

        else: # 앞선 사람의 예약 유효
            case = 2
            error = True
            return render(request,'reserve/reserve.html',{
                'Washer':Washer_,
                'error':error,
            })
            # error -> True 이면 'html딴에서 예약이 불가합니다' 메시지 올리기
    else:
        if recent_W.EndTime <= timezone.now(): #앞선 사람 이용 종료 (세탁기 아무도 안쓰는중)
            if request.method == 'POST':
                W_book = W_Book()
                W_book.MachineId = Washer_.Number
                W_book.UserId = User_.UserName
                W_book.ValidTime = timezone.now() + timedelta(minutes=10)
                W_book.save()
                return redirect('/male_308')
            
            else:
                case = 3
                error = False
                time1 = timezone.now()
                time2 = timezone.now() + timedelta(minutes=10) # 현재 이용자 예약 진행해줘야
                return render(request,'reserve/reserve.html',{
                    'Washer':Washer_,
                    'error':error,
                    'time1':time1,
                    'time2':time2,
                })
           
        elif recent_W.EndTime <= timezone.now() + timedelta(minutes=20): # 앞선 사람 이용 종료 20분 이내로 남음
            if request.method == 'POST':
                W_book = W_Book()
                W_book.MachineId = Washer_.Number
                W_book.UserId = User_.UserName
                W_book.ValidTime = recent_W.EndTime + timedelta(minutes=10)
                W_book.save()
                return redirect('/male_308')

            else:
                case = 4
                error = False
                time1 = recent_W.EndTime
                time2 = recent_W.EndTime + timedelta(minutes=10) # 현재 이용자 예약 진행해줘야
                return render(request,'reserve/reserve.html',{
                    'Washer':Washer_,
                    'error':error,
                    'time1':time1,
                    'time2':time2,
                })
        else:
            case = 5
            error = True 

            return render(request,'reserve/reserve.html',{
                'Washer':Washer_,
                'error':error,
            })

def D_reserve(request,id):
    User = get_user_model()
    Dryer_ = get_object_or_404(Dryer,pk=id)

    recent_D = D_Book.objects.filter(MachineId=Dryer_.id).order_by('-id')[0]
    recent2_D = D_Book.objects.filter(MachineId=Dryer_.id).order_by('-id')[1]

    if request.method == 'POST':
        pass
    
    return render(request,'reserve/reserve.html')
