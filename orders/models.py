from django.db import models
from users.models import User


class Order(models.Model):
    """Модель отвечает за заказы"""
    # На серевере будем работать именно с числами, но в шаблоне и а вдминке будут отображаться строковые значения
    CREATED = 0  # Обычно статусы какие-то константы указываются в начале класса
    PAID = 1  # Оплачен
    ON_WAY = 2  # В пути
    DELIVERED = 3  # Доставлен
    STATUSES = (  # Кортеж который имее в себе определенные статусы
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=256)
    basket_history = models.JSONField(default=dict)  # В нём будем хранить словарь который будет содержать в себе информацию о продуктах, связь с Bascket не возможна так как эти объекты будут удаляться после того как пользователь оформит заказ, а с моделью продуктов не можем свезать к примеру цена поменяется у продукта и получается в basket_history будет отображаться продукция с обновленной ценой. Будем хранить в json объекте что же купил пользователь.
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=STATUSES, default=CREATED)
    initiator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Oder #{self.id} - {self.first_name} {self.last_name}'
