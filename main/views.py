from django.shortcuts import render

# Create your views here.


def home(request):
    name = {
        'first_name': 'Austin',
        'second_name': 'Musuya'
    }

    return render(request, 'main/home.html', {'name': name})
