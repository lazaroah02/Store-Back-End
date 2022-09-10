from django.contrib import admin
from .models import Pedido, ListaPedido

class ListaPedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "id_producto","user","id_pedido","cantidad", "created_at",)
    list_filter = ("id_pedido",)
    
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "user","total",)    

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ListaPedido, ListaPedidoAdmin)


# Register your models here.
