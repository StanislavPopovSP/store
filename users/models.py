from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'Пользователи'
