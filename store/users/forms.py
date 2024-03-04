from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User

class UserLoginForm(AuthenticationForm):

    #переопрделим стандартные поля формы
    # username = forms.CharField(
    #     label = 'Имя',
    #     widget = forms.TextInput(attrs={"autofocus": True, 
    #                                 'class': 'form-control',
    #                                 'placeholder': 'Введите ваше имя пользователя'})
    # )
    # password = forms.CharField(
    #     label = 'Пароль',
    #     widget = forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                 'class': 'form-control',
    #                                 'placeholder': 'Введите ваш пароль'})
    # )
    #Укороченный вариант
    username = forms.CharField()
    password = forms.CharField()
    #вложенный класс для полей авторизации
    class Meta:
        model = User
        fields = ['username', 'password']
