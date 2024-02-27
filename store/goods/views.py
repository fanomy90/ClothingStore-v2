from django.shortcuts import render
from goods.models import Categories, Products

def catalog(request):
    #ojects это метод для работы с записями в БД
    #categories = Categories.objects.all()
    goods = Products.objects.all()
    context: dict[str, str] = {
        "title": "Home - Каталог ",
        "goods": goods,
        #'categories': categories,
    }
    return render(request, "goods/catalog.html", context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)
