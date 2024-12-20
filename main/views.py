from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .models import Post

# Create your views here.


@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all() # get all instances of Post class
    if request.method == 'POST':
        post_id = request.POST.get('post-id') # store the post id value from frontend to variable

        # write logic to delete post that matches the post id
        post_to_delete = Post.objects.filter(id=post_id).first()
        if post_to_delete and (post_to_delete.author == request.user or request.user.has_perm('main.delete_post')):
            post_to_delete.delete() 


    return render(request, 'main/home.html', {'posts': posts})


@login_required(login_url='/login')
@permission_required('main.add_post', login_url='/login')
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
