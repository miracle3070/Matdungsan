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