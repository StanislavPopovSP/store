from django.shortcuts import render, redirect
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm
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
                return None

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    """Функция отвечает за регистрацию"""
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                auth.login(request, user)
                return redirect('index')
            else:
                return None
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)
