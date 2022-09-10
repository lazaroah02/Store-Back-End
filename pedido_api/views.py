from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pedido, ListaPedido
from . import serializer
from rest_framework.permissions import IsAuthenticated 

# Create your views here.
class Pedido_api(APIView):
    serializer_class = serializer.PedidoSerializer
    permission_classes = [IsAuthenticated]
    #get the pedidos of the user
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
                    for pedido in Pedido.objects.filter(user = request.user)]
            return Response(pedidos, status = status.HTTP_200_OK) 
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
    
    #create a new pedido   
    def post(self, request):
        print(request.data)
        serializer_pedido = self.serializer_class(data = request.data)
        if serializer_pedido.is_valid():
            '''if request.user != serializer_pedido.validated_data["user"].id:
                return Response(status = status.HTTP_401_UNAUTHORIZED)'''
            pedido = serializer_pedido.save()
            return Response({"id_pedido":pedido.id}, status = status.HTTP_200_OK)  
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

class ListaPedido_api(APIView):
    serializer_class = serializer.ListaPedidoSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):   
        try:
            for element in request.data:        
                serializer = self.serializer_class(data = element)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(status =status.HTTP_400_BAD_REQUEST)    
            total_pedido(element["id_pedido"])    
            return Response(status =status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
def total_pedido(id_pedido):
    lista_pedido = ListaPedido.objects.filter(id_pedido = id_pedido)
    total = 0
    
    for element in lista_pedido:
        total += float(element.id_producto.precio)
    
    pedido = Pedido.objects.get(id = id_pedido)  
    pedido.total = total
    pedido.save()
          