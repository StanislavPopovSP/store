from datetime import timedelta
from http import HTTPStatus

from django.db.models import QuerySet
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from store.asgi import *
from users.models import EmailVerification, User


class UserRegistrationViewTestCase(TestCase):
    def setUp(self) -> None:
        self.data = {
            'first_name': 'Stas', 'last_name': 'Popov',
            'username': 'StasMen', 'email': 'stas.perm000@mail.ru',
            'password1': 'sjdj323jhjwewe23z', 'password2': 'sjdj323jhjwewe23z'
        }
        self.path = reverse('users:registration')
        return super().setUp()

    def user_registration_get(self) -> None:
        """Проверка получения данных станицы"""
        response = self.client.get(self.path)
        print(response)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post_success(self) -> None:
        """Проверка пользователя и верификации почты"""
        username = self.data['username']  # Проверка пользователя на существование до запроса
        self.assertFalse(User.objects.filter(username=username).exists())  # Был ли пользователь до запроса
        response = self.client.post(self.path, self.data)  # Берем последнего пользователя из фомы

        # Проверка создания пользователя
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        # self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())  # Принимает один аргумент и проверяет выражение на True, проверка пользователя на его создание

        # Проверка верификации почты
        user = User.objects.last()
        email_verification: QuerySet = EmailVerification.objects.filter(user_id=user)
        self.assertTrue(email_verification.exists())  # Проверка верификации почты для данного пользователя
        self.assertEqual(
            email_verification.first().expiration.date(),  # Дата окончания срока действия ссылки
            (now() + timedelta(hours=48)).date()
        )

        # Тест который будет выявлять ошибку(это ошибка валидации почты(email без домена), username который уже существует, пароль которткий
        # Сделаем проверку на то что username уже создан
    def test_user_registration_post_failure(self) -> None:
        """Тестирвоание ошибок"""
        User.objects.create(username=self.data['username'])  # Иметация создания пользователя, как будто пользователь с таким именем уже существует
        response = self.client.post(self.path, self.data)  # Берем последнего пользователя из фомы

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)  # Проверка сравнения ответа формы после регистрации, на ошибку
