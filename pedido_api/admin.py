from django.contrib import admin
from .models import Pedido, ListaPedido

class ListaPedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "id_producto", "id_pedido", "user", "cantidad", 'subtotal',"created_at",)
    list_filter = ("id_pedido",'user')
    
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "user","total",) 
    list_filter = ('user',)   

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ListaPedido, ListaPedidoAdmin)


# Register your models here.
