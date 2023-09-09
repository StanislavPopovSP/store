from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from store.asgi import *

class UserRegistrationViewTestCase(TestCase):

    def setUp(self) -> None:
        self.path = reverse('users:registration')
        return super().setUp()

    def user_registration_get(self):
        response = self.client.get(self.path)
        print(response)
        # self.assertEqual(response.context)
