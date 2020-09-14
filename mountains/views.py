from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your views here.

def addMountain(request):
    if request.method == "POST":
        mt_name = request.POST['mountain_name']
        mt_address = request.POST['mountain_address']
        mountain = Mountain(name=mt_name, address=mt_address)
        mountain.save()
        return redirect('index')
    return render(request, "addMountain.html")


def completeClimbing(request):
    mountains = Mountain.objects.all()
    return render(request, 'completeClimbing.html', {'mountains':mountains})
    

def searchingResult(request):
    input = request.GET['search']
    splited_str = input.split() # 검색창에 입력한 문자열을 공백을 기준으로 나눔
    san_str = "" # '산'이 들어간 문자열 저장할 곳
    for x in splited_str:
        if '산' in x:
            san_str = x
    mountain = Mountain.objects.get(name=san_str)
    return render(request, 'searchingResult.html', {'mountain':mountain})

def completeMT(request):
    user_id = int(request.POST['user_id'])
    mt_id = int(request.POST['mt_id'])
    mt_name = request.POST['mt_name']
    
    user = get_object_or_404(User, pk=user_id)
    mt = get_object_or_404(Mountain, pk=mt_id)

    com_mt = CompletedMT() # 완등한 산을 저장하는 모델
    com_mt.user_id = user
    com_mt.mountain_id = mt
    com_mt.mountain_name = mt_name
    com_mt.save()
    user.profile.complete_count += 1
    user.profile.save()    
    return redirect('index')
