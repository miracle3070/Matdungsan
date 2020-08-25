from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect, reverse, get_object_or_404

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
        return redirect('readPost')
    return render(request, 'createPost.html')

def readPost(request):
    posts = Post.objects.all()
    post_content = {'posts' : posts}
    return render(request, 'readPost.html', post_content)

def searchPost(request):
    input_text = request.GET['search']
    posts = Post.objects.all()
    search_result = []
    for post in posts:
        if input_text in post.title:
            search_result.append(post)    
    results = {'results' : search_result}
    return render(request, 'searchPost.html', results)

def deletePost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('readPost')