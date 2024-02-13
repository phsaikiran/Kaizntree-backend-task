from django import forms
from .models import Item, Category


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['sku', 'name', 'category', 'in_stock', 'available_stock']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
