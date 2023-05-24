from django.urls import path
from products.views import *

# app_name = 'products' - нужен если не сможет найти приложение если делать на главном URL namespace='products' и обращение на странице будет уже через app_name | {% url 'products:products' %} или к примеру name будет index {% url 'products:index' %}

urlpatterns = [
    path('', products, name='products')
]