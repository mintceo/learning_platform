from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registering
            return redirect('home')  # Redirect to a 'home' page or where you'd like
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

