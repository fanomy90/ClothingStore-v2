from django.contrib import admin
from django.urls import path, include
from store.settings import DEBUG

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("catalog/", include("goods.urls", namespace="catalog")),
    #path("__debug__/", include("debug_toolbar.urls")),
]
#для отладки запросов к БД
if DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
