from django.urls import path
from . import views
from django.http import HttpResponse


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('translation/', views.translation, name='translation'),
    path('chatbot/', views.chatbot, name='chatbot'),
    
]