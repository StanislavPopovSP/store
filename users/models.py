from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail


class User(AbstractUser):
    """Модель для пользователя"""
    image = models.ImageField(upload_to='users_images', null=True, blank=True)  # Добаляем поле для изображения пользователя
    is_verified_email = models.BooleanField(default=False)  # Добаляем поле которое будет отвечать подтвердил ли пользователь адрес электронной поты

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'Пользователи'


class EmailVerification(models.Model):
    """Модель для верификации адреса электронной почты"""
    code = models.UUIDField(unique=True)  # первое поле уникальный код, ссылка для пользователя. Поле которое формирует универсальный, уникальный индетефикатор, что то типо id, подойдет для нашего случая
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()  # Когда заканчивается срок действия данной ссылки

    class Meta:
        verbose_name = 'верификацию почты'
        verbose_name_plural = 'Верификация почты'

    def __str__(self) -> str:
        return f'EmailVerification object for {self.user.email}'
