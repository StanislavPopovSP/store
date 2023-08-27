from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from products.models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


class IndexView(TemplateView):
    """Отображает главную страницу"""
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, str]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Store'
        return context

# def index(request):
#     """Отображает главную страницу"""
#     context = {
#         'title': 'Store'
#     }
#     return render(request, 'products/index.html', context)


class ProductsListView(ListView):
    """Отображает страницу products.html"""
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()  # queryset - это уже сформированный список объектов Product.objects.all()
        category_id = self.kwargs.get('category_id')  # в self.kwargs хранятся дополнительные приходящие параметры
        return queryset.filter(category=category_id) if category_id else queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Store - Каталог'
        context['categories'] = ProductCategory.objects.all()
        return context

# def products(request, category_id=None, page_number=1):
#     """Отображает страницу products.html"""
#     # if category_id:
#     #     # category = ProductCategory.objects.get(id=category_id)
#     #     products = Product.objects.filter(category=category_id)
#     # else:
#     #     products = Product.objects.all()
#     # Через тернарный оператор
#     products = Product.objects.filter(category=category_id) if category_id else Product.objects.all()
#     per_page = 3
#     paginator = Paginator(products, per_page)  # per_page - сколько товаров нужно отображать на странице
#     products_paginator = paginator.page(page_number) # page() - номер страницы товара который нужно отобразить

#     context = {
#             'title': 'Store - Каталог',
#             'products': products_paginator,
#             'categories': ProductCategory.objects.all()
#         }
#     return render(request, 'products/products.html', context)

# Обработчик событий
@login_required
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


@login_required
def basket_remove(request, basket_id):
    """Удаляет корзину """
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META['HTTP_REFERER'])
