from django import template
from goods.models import Categories
#регистрируем пользовательский шаблон
register = template.Library()
#пользоавтельский шаблон для отображения категорий товаров
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()