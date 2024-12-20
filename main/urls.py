from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('logout/', views.user_logout, name='user_logout'),
    path('create-post/', views.create_post, name='create-post'),
]
