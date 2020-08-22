from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['user_password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html',
            {'error': 'username or password is incorrect'})
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
            auth.login(request, user)
            return redirect('index')
        return render(request, 'signup.html')
    return render(request, 'signup.html')