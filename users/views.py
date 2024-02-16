from django.shortcuts import render
from users.forms import LoginForm, RegistForm

def login(request):
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def registration(request):
    form = RegistForm()
    return render(request, 'users/registration.html', {'form': form})