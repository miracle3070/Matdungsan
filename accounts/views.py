from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['user_password']
        user = auth.authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html',
            {'error': '아이디 또는 비밀번호가 일치하지 않습니다.'})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')


def signup(request):
    if request.method == 'POST':
        if request.POST['user_password1'] == request.POST['user_password2']:
            user = User.objects.create_user(
                username=request.POST['user_name'], password=request.POST['user_password1'],
                email=request.POST['user_email']
            )
            gender = request.POST['gender']
            age_group = request.POST['age_group']
            complete_count = request.POST['complete_count']
            grade = request.POST['grade']
            profile = Profile(user=user, gender=gender, age_group=age_group, complete_count=complete_count, grade=grade)
            profile.save()

            auth.login(request, user)
            return redirect('index')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def loginInfo(request):
    return render(request, "loginInfo.html")