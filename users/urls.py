from django.urls import path
from users.views import login, logout
from users.views import UserRegistrationView, UpdateProfileView
from django.contrib.auth.decorators import login_required

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
    path('login/', login, name='login'),
    path('registration/ ', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', login_required(UpdateProfileView.as_view()), name='profile'),
    path('logout/', logout, name='logout')
]
