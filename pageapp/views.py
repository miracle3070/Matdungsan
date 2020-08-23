from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect, reverse

# Create your views here.

def index(request):
    posts = Post.objects.all()
    post_content = {'posts' : posts}
    return render(request, 'index.html', post_content)

def createPost(request):
    if request.method == "POST":
        title = request.POST["title"]
        image = request.FILES['image']
        content = request.POST['content']
        username = request.POST['username']
        new_post = Post(title=title, image=image, content=content, username=username)
        new_post.save()
        print("정상적으로 저장 완료!")
        return redirect('index')


    return render(request, 'createPost.html')