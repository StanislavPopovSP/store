from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import User
from users.forms import UserLoginForm, UserRegistrForm, UserProfileForm
from django.urls import reverse


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        # Проверка на валидалицию
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # Если прошла успешно проверка то аунтефицируем пользователя
            # Проверяем есть ли у нас пользователь по имени и паролю, если есть то можем двигаться дальше
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                # 1 вариант перенаправления
                return redirect('index')
                # 2 вариант перенаправления
                # return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем вы успешно зарегистрированы')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrForm()
    context = {'form': form} 
    return render(request, 'users/register.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user) 
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print(form.errors)

    else:
        form = UserProfileForm(instance=request.user) 
    
    context = {
        'title': 'Store - Профил',
        'form': form
    }
    return render(request, 'users/profile.html', context)


def logout_user(request):
    logout(request)
    redirect('index')
