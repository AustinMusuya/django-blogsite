from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def home(request):
    name = {
        'first_name': 'Austin',
        'second_name': 'Musuya'
    }

    return render(request, 'main/home.html', {'name': name})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm
    return render(request, 'registration/sign-up.html', {'form': form})


def user_logout(request):
    logout(request)  # This calls Django's logout function
    return redirect('/login')
