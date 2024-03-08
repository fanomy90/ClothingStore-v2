from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from carts.models import Cart

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            #сессионный ключ неавторизованного пользователя
            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                #уведомление пользователя о входе
                messages.success(request, f"{username}, успешно вошел на сайт")

                #когда авторизуется пользователь с заполненной корзиной по сессионном ключу то привязываем ему корзину
                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                #редирект для неавторизованного пользователя
                redirect_page = request.POST.get('netxt', None)
                if redirect_page and redirect_page != reverse('user:logout'):
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
            #сессионный ключ неавторизованного пользователя
            session_key = request.session.session_key
            #записываем в переменную введенные при регистрации данные
            user = form.instance
            #делаем автовход по сохраненным из формы регистрации данным
            auth.login(request, user)

            #когда регистрируется и авторизуется пользователь с заполненной корзиной по сессионном ключу то привязываем ему корзину
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

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
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        #отображение информации пользователя
        form = ProfileForm(instance=request.user)
    
    context = {
        'title': 'Home - Кабинет',
        'form': form
    }
    return render(request, 'users/profile.html', context)

def users_cart(request):
    return render(request, "users/users_cart.html")

#ограничение доступа для неавторизованных пользователей
@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, упешно вышел")
    auth.logout(request)
    return redirect(reverse('main:index'))
