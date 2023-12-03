from django.urls import path
from . import views
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('translation/', views.translation, name='translation'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('trans/', views.translation, name='trans'),   
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)