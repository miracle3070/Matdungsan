from django.urls import path
from . import views

app_name = 'mountains'

urlpatterns = [
    path("addMountain/", views.addMountain, name="addMountain"),
    path('completeClimbing/', views.completeClimbing, name="completeClimbing"),
    path('searchingResult/', views.searchingResult, name="searchingResult"),
    path('completeMT/', views.completeMT, name="completeMT"),
]
