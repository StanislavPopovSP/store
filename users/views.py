from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from products.models import Basket
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from users.models import User

def login(request):
    """Функция отвечает за авторизацию"""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # Или взять данные из формы которые пришли
            # username = form.data['username']
            # password = form.data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    context = {'title': 'Store - Авторизация',
               'form': form
    }
    return render(request, 'users/login.html', context)


class UserRegistrationView(CreateView):
    """Функция отвечает за регистрацию"""
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Store - Регистрация'
        return context

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
class UpdateProfileView(UpdateView):
    """Обрабатывет страницу профиль с корзиной товаров"""
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self) -> str:
        return reverse_lazy('users:profile', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Store - Личный кабинет'
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


@login_required
def logout(request):
    """Выход пользователя из сессии"""
    auth.logout(request)
    return redirect('index')
