from rest_framework import serializers
from backend.models import Item, Tag, Category


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['sku', 'name', 'category', 'in_stock', 'available_stock', 'created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'icon', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']
