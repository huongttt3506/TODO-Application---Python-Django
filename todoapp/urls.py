from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('', views.home, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login')

]