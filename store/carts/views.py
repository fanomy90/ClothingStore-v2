from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from carts.models import Cart
#from carts.utils import get_user_carts

from goods.models import Products

def cart_add(request, product_slug):
    #получаем объект товара в корзину
    product = Products.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        #запрашиваем корзину пользователя по определенному товару
        carts = Cart.objects.filter(user=request.user, product=product)
        #если товар уже есть в корзине то увеличиваем количество товара на 1 и сохраняем корзину
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
            #если корзина по доавбляемому товару не найдена то создаем ее
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    #редирект на страницу на которой был пользователь по ключу HTTP_REFERER - с какой страницы пришли
    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, cart):
    ...
def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])