from django.db import models
from django.contrib.auth import get_user_model
from store_api.models import Producto
from django.db.models import F, Sum, FloatField

User = get_user_model()

# Create your models here.

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)
    
    class Meta:
        ordering = ["id"]
        
    def __str__(self):
        return f"{self.id}"   

class ListaPedido(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default = 1)
    id_pedido = models.ForeignKey(Pedido, related_name = "lista_pedido",on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cantidad} unidades de {self.id_producto.product_name}"