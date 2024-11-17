from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.


@login_required(login_url='/login')
def home(request):
    name = {
        'first_name': 'Austin',
        'second_name': 'Musuya'
    }

    return render(request, 'main/home.html', {'name': name})


@login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        form = PostForm()
        return render(request, 'main/create-post.html', {'form': form})


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
