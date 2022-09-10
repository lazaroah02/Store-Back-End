from django.contrib import admin
from .models import Pedido, ListaPedido

class ListaPedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "id_producto","user","id_pedido","cantidad", "created_at",)
    list_filter = ("id_pedido",)

admin.site.register(Pedido)
admin.site.register(ListaPedido, ListaPedidoAdmin)


# Register your models here.
