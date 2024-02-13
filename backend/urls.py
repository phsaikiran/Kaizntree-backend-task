from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),

    path('dashboard', views.dashboard, name='Dashboard'),

    path('items', views.get_all_items, name='Get all items'),
    path('item/create', views.item_create, name='Create item'),
    path('item/<int:id>', views.get_item, name='Get item by SKU'),

    path('categories', views.get_all_categories, name='Get all categories'),
    path('category/create', views.category_create, name='Create category'),

    path('tags', views.get_all_tags, name='Get all tags'),
]
