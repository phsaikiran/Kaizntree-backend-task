from django.test import TestCase, Client
from django.contrib.auth.models import User
from backend.models import Item, Category, Tag


class APITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.category = Category.objects.create(name='Test Category')
        self.tag = Tag.objects.create(name='Test Tag')
        self.item = Item.objects.create(name='Test Item', category=self.category, in_stock=10, available_stock=5)

        self.client = Client()

    def test_get_all_items(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get('/items')
        print(response.content)

        self.assertEqual(response.status_code, 200)

    def test_item_create(self):
        self.client.login(username='testuser', password='testpassword')

        new_item_data = {
            'sku': "SKU123",
            'name': 'New Item',
            'category': self.category.id,
            'in_stock': 15,
            'available_stock': 10
        }
        response = self.client.post('/item/create', data=new_item_data)
        print(response.content)

        self.assertEqual(response.status_code, 201)

    def test_user_logout(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post('/logout')
        print(response.content)

        self.assertRedirects(response, '/login')

    def test_get_all_categories(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get('/categories')

        self.assertEqual(response.status_code, 200)

    def test_get_all_tags(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get('/tags')

        self.assertEqual(response.status_code, 200)
