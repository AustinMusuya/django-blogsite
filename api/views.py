from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, UserSerializer
from main.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

# viewset for Posts
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# viewset for Users
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
