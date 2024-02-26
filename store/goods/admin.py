from django.contrib import admin
from goods.models import Categories, Products
#регистрация моделей в админке
#admin.site.register(Categories)
#admin.site.register(Products)

#Кастомная настройка моделей в админке
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    #автоматическое заполнения поля слаг по картежу в который передали поле имя
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    #автоматическое заполнения поля слаг по картежу в который передали поле имя
    prepopulated_fields = {'slug': ('name',)}