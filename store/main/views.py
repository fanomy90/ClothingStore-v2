from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories

# Create your views here.
def index(request):
    context: dict = {
        'title': 'Главная',
        'content': 'Магазин одежды',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context: dict = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'Здесь могла быть ваша реклама'
    }
    return render(request, 'main/about.html', context)