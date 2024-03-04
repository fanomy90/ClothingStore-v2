from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from django.http import HttpResponseRedirect

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                #уведомление пользователя о входе
                messages.success(request, f"{username}, успешно вошел на сайт")
                #редирект для неавторизованного пользователя
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            #записываем в переменную введенные при регистрации данные
            user = form.instance
            #делаем автовход по сохраненным из формы регистрации данным
            auth.login(request, user)
            messages.success(request, f"{user.username}, успешно зарегистрировался и вошел на сайт")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)

#ограничение доступа для неавторизованных пользователей
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Пользователь упешно обновлен")
            return HttpResponseRedirect(reverse('main:profile'))
    else:
        #отображение информации пользователя
        form = ProfileForm(instance=request.user)
    
    context = {
        'title': 'Home - Кабинет',
        'form': form
    }
    return render(request, 'users/profile.html', context)

#ограничение доступа для неавторизованных пользователей
@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, упешно вышел")
    auth.logout(request)
    return redirect(reverse('main:index'))
