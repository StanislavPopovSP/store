from typing import Any

from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from users.models import User
from users.tasks import settings_email_verification


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'placeholder': "Введите имя пользователя"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4", 'placeholder': "Введите пароль"}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'placeholder': "Введите имя"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'placeholder': "Введите фамилию"}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'placeholder': "Введите имя пользователя"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': "form-control py-4", 'placeholder': "Введите адрес эл. почты"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4", 'placeholder': "Введите пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4", 'placeholder': "Подтвердите пароль"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    # Данный метод отрабатывается в тот момент когда создается объект пользователя, данный метод в данном примере возвращает объект USER
    # Метод создает для пользователя уникальный ключ для отправки его на почту для верификации
    def save(self, commit: bool = ...) -> Any:
        """Метод получает пользователя из формы и отправлем ему письмо на почту"""
        user = super().save(commit)
        settings_email_verification.delay(user.pk)  # Если вызывать () то задача не будет обработана паралельно, метод delay нужен для паралельной отправки
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4"}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': "custom-file-label", 'placeholder': "Выберите изображение"}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'readonly': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': "form-control py-4", 'readonly': True}))  # readonly только для чтения а не для редактирования

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
