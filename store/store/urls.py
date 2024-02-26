from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from store import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("catalog/", include("goods.urls", namespace="catalog")),
    #path("__debug__/", include("debug_toolbar.urls")),
]
#для отладки запросов к БД
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)