from django.shortcuts import render, redirect
from users.models import User
from users.forms import UserLoginForm
from django.contrib import auth


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
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    """Функция отвечает за регистрацию"""
    return render(request, 'users/registration.html')
