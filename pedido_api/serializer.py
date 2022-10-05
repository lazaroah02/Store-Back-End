from rest_framework import serializers
from .models import Pedido, ListaPedido
from store_api.models import Producto
from django.contrib.auth import get_user_model
User = get_user_model()

class PedidoSerializer(serializers.ModelSerializer):
     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
     
     class Meta:
            model = Pedido
            fields = ['user']

class ListaPedidoSerializer(serializers.ModelSerializer):
    id_pedido = serializers.PrimaryKeyRelatedField(queryset=Pedido.objects.all()) 
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    id_producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())
    cantidad = serializers.IntegerField(default = 1)
    subtotal = serializers.FloatField(default = 0)
    
    class Meta:
        model = ListaPedido
        fields = ["id_producto","id_pedido","user", "cantidad", 'subtotal']
                