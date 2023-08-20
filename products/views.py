from django.shortcuts import render, redirect
from products.models import Product, ProductCategory, Basket
from users.models import User


def index(request):
    """Отображает главную страницу"""
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    """Отображает страницу products.html"""
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)

# Обработчик событий
def basket_add(request, product_id):
    """Добавляет товар в корзину"""
    product = Product.objects.get(id=product_id)  #  берем продукт который выбрали
    baskets = Basket.objects.filter(user=request.user, product=product)  # 1 параметр должны взять все элементы корзины которые принадлежат пользователю который выполняет запрос и взять корзину с данным продуктом

    # Если у пользователя корзина пустая(Query SET пустой)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        # Если объект есть, мы просто добавляем предыдущий на один, новый не создаем
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    # Когда действие выполнилось надо пользователя куда-то вернуть, на какой странице находится пользователь туда и вернуть
    return redirect(request.META['HTTP_REFERER']) # -> страница где было выполнено действие
    # return redirect(request.path) # -> страница на то что было направлено действие
