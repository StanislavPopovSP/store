from django.contrib import admin
from users.models import User
from products.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    inlines = (BasketAdmin,) # BasketAdmin - будем отображатьв админке пользователя, сразу когда будем заходить на страницу пользователя сразу будем видеть какие товары у него были добавлены в корзину. (Корзину прикрутили для пользователя)
