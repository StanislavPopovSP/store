from django.db import models
from users.models import User

class ProductCategory(models.Model):
    """Таблица категорий"""
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta: # Отвечает за доп настройки
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

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

    class Meta: # Отвечает за доп настройки
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
            return f'Продукт: {self.name} | Категория: {self.category.name}'


# Можем создать новый менеджер, он будет наследовать все методы которые уже имеются, создадим свой метод который можем вызывать в шаблонах
class BasketQuerySet(models.QuerySet):
    # self будет обращаться уже ко всему классу(всем объектам сразу)
    def total_sum(self):
        """Метод возвращает общую сумму в корине товаров для пользователя"""
        return sum([basket.sum() for basket in self])

    def total_quantity(self):
        """Метод возвращает общее количество товаров для пользователя"""
        return sum([basket.quantity for basket in self])


class Basket(models.Model):
    """Таблица для корзины товаров"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestapp = models.DateTimeField(auto_now_add=True)

    # Нужно переопределить objects, расширить добавленные методы
    objects = BasketQuerySet.as_manager()

    def __str__(self) -> str:
         return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    def sum(self):
        """Метод возвращает сумму выбранного количества товаров в корзине """
        return self.quantity * self.product.price

    # def total_sum(self):
    #     """Метод возвращает общую сумму в корине товаров для пользователя"""
    #     baskets = Basket.objects.filter(user=self.user)
    #     return sum([basket.summ() for basket in baskets])

    # def total_quantity(self):
    #     """Метод возвращает общее количество товаров для пользователя"""
    #     baskets = Basket.objects.filter(user=self.user)
    #     return sum([basket.quantity for basket in baskets])
