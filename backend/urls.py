from django.urls import path
from . import views

urlpatterns = [
    path('user', views.get_all_users, name='Get all users'),
    path('user/create', views.user_create, name='Create user'),
    path('user/<str:pk>', views.get_user, name='Get user by ID'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
