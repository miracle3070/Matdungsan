from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('createPost/', views.createPost, name='createPost'),
    path('readPost/', views.readPost, name='readPost'),
    path('searchPost/', views.searchPost, name='searchPost'),
    path('deletePost/<int:post_id>', views.deletePost, name='deletePost'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
