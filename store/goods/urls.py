from django.urls import path
from goods import views
app_name = 'goods'
urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    #маршрут с пагинацией
    path('<slug:category_slug>/<int:page>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    #path('product/<int:product_id>/', views.product, name='product'),
]