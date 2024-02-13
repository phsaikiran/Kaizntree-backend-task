from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.models import Item, Category, Tag
from .forms import ItemForm, CategoryForm
from .serializers import ItemSerializer, CategorySerializer, TagSerializer


@login_required
@api_view(['GET'])
def get_all_items(request):
    """
    Get a list of items based on optional filters.
    Parameters:
        - category_id (optional): Filter items by category ID.
        - in_stock_min (optional): Minimum value for in-stock items.
        - in_stock_max (optional): Maximum value for in-stock items.
        - available_stock_min (optional): Minimum value for available stock.
        - available_stock_max (optional): Maximum value for available stock.
        - search (optional): Search items by name (case-insensitive).
    Response:
        - Status Code: 200 OK
        - Body: Array of serialized Item objects.
    """
    category_id = request.GET.get('category_id')
    in_stock_min = request.GET.get('in_stock_min')
    in_stock_max = request.GET.get('in_stock_max')
    available_stock_min = request.GET.get('available_stock_min')
    available_stock_max = request.GET.get('available_stock_max')
    search = request.GET.get('search')
    print(category_id, in_stock_min, in_stock_max, available_stock_min, available_stock_max, search)

    filters = {}
    if category_id:
        filters['category__id'] = category_id
    if in_stock_min:
        filters['in_stock__gte'] = in_stock_min
    if in_stock_max:
        filters['in_stock__lte'] = in_stock_max
    if available_stock_min:
        filters['available_stock__gte'] = available_stock_min
    if available_stock_max:
        filters['available_stock__lte'] = available_stock_max
    if search:
        filters['name__icontains'] = search

    items = Item.objects.filter(**filters)

    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@login_required
@api_view(['GET', 'POST'])
def item_create(request):
    """
    Create a new item.
    Method:
        - POST
    Authentication:
        - Login required
    Request Body:
        - JSON object representing the item to be created. See ItemSerializer for the expected format.
    Response:
        - Status Code:
            - 201 Created: Item created successfully.
            - 400 Bad Request: Invalid input data.
    """

    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
    else:
        form = ItemForm()

    return render(request, 'item_create.html', {'form': form})


@login_required
@api_view(['GET'])
def get_item(request, id):
    """
    Get an item by ID.
    Method:
        - GET
    Authentication:
        - Login required
    Parameters:
        - id: ID of the item to retrieve.
    Response:
        - Status Code:
            - 200 OK: Item found, returns serialized Item object.
            - 404 Not Found: Item not found.
    """

    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return Response({'message': 'Item not found'}, status=404)

    serializer = ItemSerializer(item, many=False)
    return Response(serializer.data)


@login_required
@api_view(['GET'])
def get_all_categories(request):
    """
    Get a list of all categories.
    Method:
        - GET
    Authentication:
        - Login required
    Response:
        - Status Code: 200 OK
        - Body: Array of serialized Category objects.
    """

    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@login_required
@api_view(['GET', 'POST'])
def category_create(request):
    """
    Create a new category.
    Method:
        - POST
    Authentication:
        - Login required
    Request Body:
        - JSON object representing the category to be created. See CategorySerializer for the expected format.
    Response:
        - Status Code:
            - 201 Created: Category created successfully.
            - 400 Bad Request: Invalid input data.
    """

    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
    else:
        form = CategoryForm()

    return render(request, 'category_create.html', {'form': form})


@login_required
@api_view(['GET'])
def get_all_tags(request):
    """
    Get a list of all tags.
    Method:
        - GET
    Authentication:
        - Login required
    Response:
        - Status Code: 200 OK
        - Body: Array of serialized Tag objects.
    """

    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)


@login_required
def dashboard(request):
    """
    Get the user's dashboard.
    Method:
        - GET
    Authentication:
        - Login required
    Response:
        - Status Code: 200 OK
        - Body: HTML content for the dashboard.
    """

    if request.method != 'GET':
        return Response({'message': 'Method not allowed'}, status=405)
    return render(request, 'dashboard.html')


def register(request):
    """
    Register a new user.
    Method:
        - POST
    Request Body:
        - Form data for user registration. See UserCreationForm for the expected format.
    Response:
        - Status Code: 302 Found (redirects to /dashboard/ on successful registration)
    """

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
    """
    Log in a user.
    Method:
        - POST
    Request Body:
        - Form data for user login. See AuthenticationForm for the expected format.
    Response:
        - Status Code: 302 Found (redirects to /dashboard/ on successful login)
    """

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    """
    Log out the user.
    Method:
        - GET
    Authentication:
        - Login required
    Response:
        - Status Code: 302 Found (redirects to /login/ on successful logout)
    """

    logout(request)
    return redirect('/login')
