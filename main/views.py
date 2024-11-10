from django.shortcuts import render
from .forms import RegisterForm

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
    else:
        form = RegisterForm
    return render(request, 'registration/sign-up.html', {'form': form})
