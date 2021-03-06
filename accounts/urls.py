from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('loginInfo/', views.loginInfo, name="loginInfo"),
    path('myCompletedMT/', views.myCompletedMT, name="myCompletedMT"),
]
