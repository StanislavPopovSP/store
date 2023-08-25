from django.contrib import admin
from products.models import Product, ProductCategory, Basket


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')  # Отвечает за отображение полей в админке
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')  # Перечисление полей в нутри таблицы. ('price', 'quantity')  - сделали на одной строке
    # readonly_fields = ('description',)  # переменная будет доступна только для чтения
    search_fields = ('name',)  # для поиска полей
    ordering = ('name',)  # отсортировать(в алфавитном порядке)


# TabularInline - BasketAdmin будет чатью другой админки, его можно применять если есть ForeignKey связь
class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestapp')
    readonly_fields = ('created_timestapp',)  # Для отображения времени, которое не должно меняться, нужно добавить readonly_fields
    extra = 0  # отвечает за дополнительные поля для добовления, default = 3
