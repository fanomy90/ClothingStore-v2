from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from carts.models import Cart
from carts.utils import get_user_carts

from goods.models import Products

def cart_add(request):
    product_id = request.POST.get("product_id")
    #получаем объект товара в корзину
    product = Products.objects.get(id=product_id)
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
    #работа с jquery для перерисовки корзины без обновления страницы
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        #формируем часть разметки шаблона в виде строки и контекст в виде словаря для перерисовки с помощью jquery
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request
    )
    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }
    return JsonResponse(response_data)

def cart_change(request, cart):
    ...
def cart_remove(request):
    #получаем данные из post запроса
    cart_id = request.POST.get("cart_id")
    #собираем данные для контекста
    #получаем экзепляр объекта корзины из модели по id
    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()
    #работа с jquery для перерисовки корзины без обновления страницы
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        #формируем часть разметки шаблона в виде строки и контекст в виде словаря для перерисовки с помощью jquery
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)
    #собираем контекст для передачи в jquery
    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }
    return JsonResponse(response_data)