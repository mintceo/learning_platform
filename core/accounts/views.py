
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import user_logged_out
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the new user instance
            return redirect('login.html')  # Redirect to a login page, for example
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



def home(request):
    return render(request, 'home.html')

def root(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirects to the named URL 'home'
    else:
        return redirect('register')  