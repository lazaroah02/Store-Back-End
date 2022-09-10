from django.contrib import admin
from django.urls import path,include
from authentication_api import urls as authentication_urls
from store_api import urls as store_urls
from pedido_api import urls as pedido_urls

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include(authentication_urls)),
    path('store/', include(store_urls)),
    path('pedido/', include(pedido_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
