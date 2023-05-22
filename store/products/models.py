from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)  # max_digits - сколько может быть максимально цифр до запятой, decimal_places- после запятой
    quantity = models.PositiveIntegerField(default=0)  # кол-во товаров на складе
    image = models.ImageField(upload_to='products_images/')
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)  # Категорию невозможно будет удалить, пока не удалятся все продукты данной категории.

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
