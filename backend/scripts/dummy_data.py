from django.utils import timezone
from backend.models import Category, Item, Tag, TagItem


def run():
    # Create categories
    category1 = Category.objects.create(name='Electronics')
    category2 = Category.objects.create(name='Clothing')
    category3 = Category.objects.create(name='Books')

    # Create tags
    tag1 = Tag.objects.create(name='⚡️', icon='⚡️')
    tag2 = Tag.objects.create(name='😎', icon='😎')
    tag3 = Tag.objects.create(name='💻', icon='💻')

    # Create items
    item1 = Item.objects.create(
        sku='SKU001',
        name='Laptop',
        category=category1,
        in_stock=50,
        available_stock=50,
        created_at=timezone.now(),
        updated_at=timezone.now()
    )

    item2 = Item.objects.create(
        sku='SKU002',
        name='T-shirt',
        category=category2,
        in_stock=100,
        available_stock=100,
        created_at=timezone.now(),
        updated_at=timezone.now()
    )

    item3 = Item.objects.create(
        sku='SKU003',
        name='Python Programming Book',
        category=category3,
        in_stock=30,
        available_stock=30,
        created_at=timezone.now(),
        updated_at=timezone.now()
    )

    # Create tag-item associations
    tag_item1 = TagItem.objects.create(sku=item1, tag=tag1, created_at=timezone.now(), updated_at=timezone.now())
    tag_item2 = TagItem.objects.create(sku=item2, tag=tag2, created_at=timezone.now(), updated_at=timezone.now())
    tag_item3 = TagItem.objects.create(sku=item3, tag=tag3, created_at=timezone.now(), updated_at=timezone.now())
    tag_item4 = TagItem.objects.create(sku=item1, tag=tag3, created_at=timezone.now(), updated_at=timezone.now())

    print("Dummy data created successfully.")
