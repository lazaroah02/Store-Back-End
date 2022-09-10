from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pedido, ListaPedido
from . import serializer
from django.shortcuts import redirect

# Create your views here.
class Pedido_api(APIView):
    serializer_class = serializer.PedidoSerializer
    def get(self, request):
        try:
            pedidos = [{"id":pedido.id,
                    "user":pedido.user.email,
                    "lista_pedido":[{
                              "id_producto":lista_pedido.id_producto.id,  
                              "producto":lista_pedido.id_producto.product_name,
                              "precio":lista_pedido.id_producto.precio,
                              "cantidad":lista_pedido.cantidad,}
                             for lista_pedido in ListaPedido.objects.filter(id_pedido = pedido.id)],
                    "total":pedido.total,
                    "created":pedido.created_at
                    }
                    for pedido in Pedido.objects.all()]
            return Response(pedidos, status = status.HTTP_200_OK) 
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
            serializer_pedido = self.serializer_class(data = request.data)
            if serializer_pedido.is_valid():
                serializer_pedido.save()
                return redirect(to="/pedidos/lista-pedido/")   

class ListaPedido_api(APIView):
    coste_total = 0
    serializer_class = serializer.ListaPedidoSerializer
    def post(self, request):   
        try:
            for element in request.data:        
                serializer = self.serializer_class(data = element)
                if serializer.is_valid():
                    serializer.save()
                    print(serializer.validated_data["id_producto"].precio)
                else:
                    print(serializer.errors)
                    return Response(status =status.HTTP_500_INTERNAL_SERVER_ERROR)    
            return Response(status =status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)