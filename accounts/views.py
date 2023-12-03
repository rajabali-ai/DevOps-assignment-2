from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .forms import uploaded_videoForm
from .models import uploaded_video
from django.contrib.auth.decorators import login_required


def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # You can change 'login' to the desired URL name for login
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')



def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # You can change 'home' to the desired URL name for the logged-in user's home page
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def translation(request):
    videos = uploaded_video.objects.filter(user=request.user)
    if request.method == 'POST':
        form = uploaded_videoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('trans.html') 
    else:
        form = uploaded_videoForm()
    return render(request, 'trans.html', {'form': form, 'videos': videos})



def chatbot(request):
    return render(request, 'chatbot.html')

