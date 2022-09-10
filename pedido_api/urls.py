from django.urls import path
from .views import Pedido_api, ListaPedido_api

urlpatterns = [
    path('', Pedido_api.as_view()),
    path('lista-pedido/', ListaPedido_api.as_view()),
]
