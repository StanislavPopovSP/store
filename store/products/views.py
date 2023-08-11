from django.shortcuts import render


def index(request):
    """Отображает главную страницу"""
    return render(request, 'products/index.html')


def products(request):
    """Отображает страницу products.html"""
    return render(request, 'products/products.html')
