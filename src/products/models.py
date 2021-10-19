from django.db import models

from src.api.services import get_path_upload


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to=get_path_upload
    )
    category_name = models.CharField(max_length=150, default='')

    def __str__(self):
        return f'{self.product_name}'


# class Category(models.Model):
#     category_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.category_name}'