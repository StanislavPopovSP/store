from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from store.asgi import *
from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):

    def test_view(self) -> None:
        """Проверка представления IndexView"""
        path = reverse('index')  # проверка пути
        response = self.client.get(path)  # client это вспомогательный класс который помогает обращаться к различным методам
        # print(response)

        self.assertEqual(response.status_code, HTTPStatus.OK)  # Метод для сравнения
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html')  # Какой шаблон у нас используется


class ProductsListViewTestCase(TestCase):
    fixtures = ['categories.json', 'products.json']

    def setUp(self) -> None:
        """Метод для повторяющихся переменных"""
        self.products = Product.objects.all()
        self.category = ProductCategory.objects.first()
        return super().setUp()

    def test_list(self) -> None:
        """Тестирование списка продуктов, статуса, заголока"""
        path = reverse('products:products')
        response = self.client.get(path)  # при запросе get на эту страницу
        self._common_tests(response)
        self.assertEqual(list(response.context_data['object_list']), list(self.products[:3]))  # QuarySET сравнить не получится, т.к данный объект создается в разное время, по разному сформированы.

    def test_list_with_category(self) -> None:
        """Тестирование выделенной категории, статуса, заголока"""
        path = reverse('products:category', kwargs={'category_id': self.category.id})
        response = self.client.get(path)  # Придет выделенная категория
        self._common_tests(response)
        self.assertEqual(
            list(response.context_data['object_list']),  # Сравнение то что пришло клиенту
            list(self.products.filter(category=self.category.id)))  # То что пришло из БД

    def _common_tests(self, response) -> None:
        """Метод для повторяющихся проверок"""
        self.assertEqual(response.status_code, HTTPStatus.OK)  # Возвращается статус 200
        self.assertEqual(response.context_data['title'], 'Store - Каталог')
        self.assertTemplateUsed(response, 'products/products.html')  # Правильно используется шаблон
