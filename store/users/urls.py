from django.urls import path
from users.views import *

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('profile/', profile, name='profile')
]
