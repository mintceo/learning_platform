
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def home(request):
    return render(request, 'accounts/home.html')

def root(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirects to the named URL 'home'
    else:
        return redirect('register')  