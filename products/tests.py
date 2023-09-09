from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from store.asgi import *

class IndexViewTestCase(TestCase):

    def test_view(self) -> None:
        """Проверка представления IndexView"""
        path = reverse('index')  # проверка пути
        response = self.client.get(path)  # client это вспомогательный класс который помогает обращаться к различным методам
        print(response)

        self.assertEqual(response.status_code, HTTPStatus.OK)  # Метод для сравнения
        self.assertEqual(response.context_data['title'], 'Store')
        # self.assertTemplateUsed(response, 'products/index.html')  # Какой шаблон у нас используется
