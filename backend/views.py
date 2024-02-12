from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.models import Item, Category, Tag
from .serializers import ItemSerializer, CategorySerializer, TagSerializer


@login_required
@api_view(['GET'])
def get_all_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@login_required
@api_view(['GET'])
def get_item(request, sku):
    try:
        item = Item.objects.get(sku=sku)
    except Item.DoesNotExist:
        return Response({'message': 'Item not found'}, status=404)

    serializer = ItemSerializer(item, many=False)
    return Response(serializer.data)


@login_required
@api_view(['GET'])
def get_all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@login_required
@api_view(['GET'])
def get_all_tags(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)


# @login_required
# @api_view(['POST'])
# def user_create(request):
#     # Hash the password before saving it to the database
#     request.data['password'] = make_password(request.data['password'])
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     else:
#         return Response(serializer.errors, status=400)

@login_required
def dashboard(request):
    if request.method != 'GET':
        return Response({'message': 'Method not allowed'}, status=405)
    return render(request, 'dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/login')
