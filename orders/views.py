from django.shortcuts import render
from common.views import TitleMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView


class OrderCreateView(TitleMixin, TemplateView):
    """Оформление заказа"""
    template_name = 'orders/order-create.html'
    title = 'Store - Оформление заказа'
