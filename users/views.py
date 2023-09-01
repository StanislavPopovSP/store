from typing import Any, Dict
from django import http
from django.http import HttpRequest, HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin

from products.models import Basket
from users.models import User, EmailVerification
from common.views import TitleMixin

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


# С примененнием представлений
class UserLoginView(TitleMixin, LoginView):
    """Отвечает за авторизацию"""
    template_name = 'users/login.html'
    authentication_form = UserLoginForm
    title = 'Store - Авторизация'

# С применением функций
# def login(request):
#     """Функция отвечает за авторизацию"""
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             # Или взять данные из формы которые пришли
#             # username = form.data['username']
#             # password = form.data['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return redirect('index')
#     else:
#         form = UserLoginForm()
#     context = {'title': 'Store - Авторизация',
#                'form': form
#     }
#     return render(request, 'users/login.html', context)


# С примененнием представлений
class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    """Функция отвечает за регистрацию"""
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляем! Вы успешно зарегистррованы!'
    title = 'Store - Регистрация'


# С применением функций
# def registration(request):
#     """Функция отвечает за регистрацию"""
#     if request.method == "POST":
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             messages.success(request, 'Поздравляем! Вы успешно зарегистррованы!')
#             if user:
#                 auth.login(request, user)
#                 return redirect('index')
#     else:
#         form = UserRegistrationForm()
#     context = {'title': 'Store - Регистрация',
#                'form': form
#                }
#     return render(request, 'users/registration.html', context)


# С примененнием представлений
class UpdateProfileView(TitleMixin, UpdateView):
    """Обрабатывет страницу профиль с корзиной товаров"""
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Личный кабинет'

    def get_success_url(self) -> str:
        return reverse_lazy('users:profile', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

# С применением функций
# @login_required
# def profile(request):
#     """Обрабатывет страницу профиль с корзиной товаров"""
#     user = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('users:profile')
#     else:
#         form = UserProfileForm(instance=user)

#     baskets = Basket.objects.filter(user=request.user)
#     # total_sum = 0
#     # total_quantity = 0
#     # for basket in baskets:
#     #     total_sum += basket.summ()
#     #     total_quantity += basket.quantity
#     # Или через генераторы, но что бы не нагружать обработчик перенесем в класс данные методы
#     # total_sum = sum([basket.summ() for basket in baskets])
#     # total_quantity = sum([basket.quantity for basket in baskets])
#     context = {'title': 'Store - Личный кабинет',
#                'form': form,
#                'baskets': baskets,
#             #    'total_quantity': total_quantity,
#             #    'total_sum': total_sum
#                }
#     return render(request, 'users/profile.html', context)


class EmailVerificationView(TitleMixin, TemplateView):
    """Проверяет входящие данные, верификация email """
    title = 'Store - Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        code = kwargs['code']
        user = User.objects.get(email=self.kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        # Если данные пришли
        if email_verification.exists():
            user.is_verified_email = True
            user.save()
            return super().get(request, *args, **kwargs)
        # Если не пришли, то перенаправит на главную страницу
        else:
            return redirect('index')

# @login_required
# def logout(request):
#     """Выход пользователя из сессии"""
#     auth.logout(request)
#     return redirect('index')
