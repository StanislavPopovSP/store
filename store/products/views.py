from django.shortcuts import render


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
        'products': [
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
                'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                'name': 'Синяя куртка The North Face',
                'price': 23725,
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
            }
        ]
    }
    return render(request, 'products/products.html', context)
