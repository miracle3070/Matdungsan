from django.urls import path
from . import views

app_name = 'mountains'

urlpatterns = [
    path("addMountain/", views.addMountain, name="addMountain"),

]
