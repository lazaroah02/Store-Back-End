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
                              "precio":lista_pedido.id_producto.precio,
                              "cantidad":lista_pedido.cantidad,
                              'subtotal':lista_pedido.subtotal,}
                             for lista_pedido in ListaPedido.objects.get(id_pedido = pedido.id)],
                    "total":pedido.total,
                    "created":pedido.created_at
                    }
                    for pedido in Pedido.objects.filter(user = request.user)]
            return Response(pedidos, status = status.HTTP_200_OK) 
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
    
    #create a new pedido   
    def post(self, request):
        serializer_pedido = self.serializer_class(data = {'user':request.user.id})
        if serializer_pedido.is_valid():
            pedido = serializer_pedido.save()
            return Response({"id_pedido":pedido.id}, status = status.HTTP_201_CREATED)  
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

#list with the products of the pedido
class ListaPedido_api(APIView):
    serializer_class = serializer.ListaPedidoSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            total = 0
            for element in request.data['lista_pedido']:  
                serializer = self.serializer_class(data = {
                                                        'id_pedido':request.data['id_pedido'],
                                                        'user':request.user.id,
                                                        'id_producto':element['id'],
                                                        'cantidad':element['cantidad'],
                                                        'subtotal':element['subtotal'],})
                if serializer.is_valid():
                    serializer.save()
                    total += element['subtotal']
                else:
                    return Response(status =status.HTTP_400_BAD_REQUEST)  
            total_pedido(request.data['id_pedido'], total)    
            return Response(status =status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
def total_pedido(id_pedido, total):
    pedido = Pedido.objects.get(id = id_pedido) 
    pedido.total = total
    pedido.save()
          