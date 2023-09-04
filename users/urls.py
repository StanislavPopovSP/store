from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (EmailVerificationView, UpdateProfileView,
                         UserLoginView, UserRegistrationView)

app_name = 'users'

# Через функции
# urlpatterns = [
#     path('login/', login, name='login'),
#     path('registration/ ', registration, name='registration'),
#     path('profile/', profile, name='profile'),
#     path('logout/', logout, name='logout')
# ]

# Через представления
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/ ', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', login_required(UpdateProfileView.as_view()), name='profile'),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification')  # передаем email, т.к нужно определить (пользователь получает электронное письмо себе в почтовый адрес, переходит по ссылке мы не можем определить что это за пользователь поэтому берем email и code)

]
