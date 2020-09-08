from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

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