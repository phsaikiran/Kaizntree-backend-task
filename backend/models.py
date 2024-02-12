from django.db import models


class Item(models.Model):
    sku = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    in_stock = models.IntegerField(null=False, blank=False)
    available_stock = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    icon = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    icon = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
