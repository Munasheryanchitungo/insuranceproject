from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView  # Add this import
from .forms import UserRegisterForm

# Add this CustomLoginView class
class CustomLoginView(LoginView):
    template_name = 'users/login.html'

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')