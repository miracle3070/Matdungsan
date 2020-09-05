from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def addMountain(request):
    if request.method == "POST":
        return HttpResponse("잘 되네!")
    return render(request, "addMountain.html")