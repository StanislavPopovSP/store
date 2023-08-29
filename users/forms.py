from typing import Any
import uuid
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.utils.timezone import now  # Можно из джанго взять текущее время

from users.models import User, EmailVerification


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
        user = super().save(commit)
        # Будем формировать логику, которая отправляет электронное письмо, на адрес электронной почты пользователя, с просьбой подтвердить адрес с его электронной почтой
        expiration = now() + timedelta(hours=48)
        code = uuid.uuid4()
        # Будет создаваться каждый раз EmailVerification при регистрации нового пользователя
        record = EmailVerification.objects.create(code=code, user=user, expiration=expiration)
        record.send_verification_email()
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
        'class': "form-control py-4", 'readonly': True})) # readonly только для чтения а не для редактирования
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
