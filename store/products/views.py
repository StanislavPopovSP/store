from django.shortcuts import render


def index(request):
    """Отображает главную страницу"""
    return render(request, 'products/index.html')
