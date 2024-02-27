from django.shortcuts import get_list_or_404, render 
from goods.models import Categories, Products
from django.core.paginator import Paginator

def catalog(request, category_slug):
    page = request.GET.get('page', 1)
    if category_slug == 'all':
    #ojects это метод для работы с записями в БД
    #Использование фильтра при выводе товара по категориям
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
        #goods = Products.objects.filter(category__slug=category_slug)
    #пагинатор
    paginator = Paginator(goods, 9)
    current_page = paginator.page(int(page))

    context: dict[str, str] = {
        "title": "Home - Каталог ",
        "goods": current_page,
        "slug_url": category_slug,
        #'categories': categories,
    }
    return render(request, "goods/catalog.html", context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)
