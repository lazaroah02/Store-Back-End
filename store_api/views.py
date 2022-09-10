from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from .models import Producto, Categoria

# Create your views here.

class Store(APIView):
    def get(self, request, category_id = None):
        try:
            #si no recive una categoria por url devuelve todos los productos
            if category_id == None: 
                productos = [{"id":producto.id, 
                              "name":producto.product_name, 
                              "description":producto.product_description, 
                              "precio":producto.precio,
                              "foto":producto.product_img.url,
                              "category_id":producto.categoria.id,
                              "category_name":producto.categoria.nombre, 
                              "updated":producto.updated_at} 
                             for producto in Producto.objects.all()]
                return Response(productos, status = status.HTTP_200_OK)
            
            #devuelve los productos que pertenecen a la categoria recivida por url
            else: 
                productos = [{"id":producto.id, 
                              "name":producto.product_name, 
                              "description":producto.product_description, 
                              "precio":producto.precio,
                              "foto":producto.product_img.url,
                              "category_id":producto.categoria.id,
                              "category_name":producto.categoria.nombre, 
                              "updated":producto.updated_at} 
                             for producto in Producto.objects.filter(categoria = category_id)]
                if productos == []:
                    return Response(status = status.HTTP_404_NOT_FOUND)
                else:
                    return Response(productos, status = status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
   