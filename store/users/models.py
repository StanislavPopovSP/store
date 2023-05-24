from django.db import models
from django.contrib.auth.models import AbstractUser # Расширяет возможности в админ панели пользователя
# Когда проект создается принимается решение будем ли мы работать с существующей таблицей пользователей или мы будем расширять свою

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
