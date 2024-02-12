from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('dashboard/', views.dashboard, name='Dashboard'),

    path('items/', views.get_all_items, name='Get all items'),
    path('categories/', views.get_all_categories, name='Get all categories'),
    path('tags/', views.get_all_tags, name='Get all tags'),

    # path('item/create', views.user_create, name='Create user'),
    path('item/<str:sku>', views.get_item, name='Get item by SKU'),
]
