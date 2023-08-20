from django.db import models
from users.models import User

class ProductCategory(models.Model):
    """Таблица категорий"""
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    """Таблица какого-то продукта"""
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)  # max_digits - сколько может быть максимально цифр до запятой, decimal_places- после запятой
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images/')
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)  # Категорию невозможно будет удалить, пока не будут удалены все продукты данной категории.

    def __str__(self):
            return f'Продукт: {self.name} | Категория: {self.category.name}'


class Basket(models.Model):
    """Таблица для корзины товаров"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestapp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
         return f'Корзина для {self.user.email} | Продукт: {self.product.name}'
