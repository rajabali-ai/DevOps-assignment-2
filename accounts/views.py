from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # You can change 'login' to the desired URL name for login
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.email = form.cleaned_data.get('email')
#             user.save()
#             login(request, user)
#             return redirect('dashboard')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})



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

def translation(request):
    return render(request, 'translation.html')

def chatbot(request):
    return render(request, 'chatbot.html')