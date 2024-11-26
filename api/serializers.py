from django.contrib.auth import get_user_model
from main.models import Post
from rest_framework.serializers import ModelSerializer

User = get_user_model()

# serializer class for Post model

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# serializer class form User model

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'