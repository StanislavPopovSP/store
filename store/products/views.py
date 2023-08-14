from django.shortcuts import render
from products.models import Product, ProductCategory


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
