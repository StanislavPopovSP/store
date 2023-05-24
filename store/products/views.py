from django.shortcuts import render
from products.models import Product, ProductCategory


def index(request) -> str | bool:
    context = {
        'title': 'Test title',
        'is_promotion': False,
    }
    return render(request, 'products/index.html', context)


def products(request) -> str | object | object:
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
