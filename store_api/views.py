from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from django.core.paginator import Paginator
from .models import Producto, Categoria, Video

# Create your views here.
class GetCategories(APIView):
    def get(self, request):
        categories = [{
            "id":category.id,
            "name":category.nombre,}
             for category in Categoria.objects.all()]
        if categories == []:
            return Response([],status=status.HTTP_404_NOT_FOUND)
        return Response(categories, status=status.HTTP_200_OK)
 
class VideoView(APIView):
    def get(self, request):
        try:
            video = [{"id":vid.id,
                    "video":vid.video.url}
                    for vid in Video.objects.all()]
            return Response(video, status=status.HTTP_200_OK)
        except:
            return Response([], status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class SearchAnProductView(APIView):
    def get(self, request, name_product = None):
        try:
            #search a product for his name in capitalize()
            if name_product != None:
                product = [{"id":producto.id, 
                              "name":producto.product_name, 
                              "description":producto.product_description, 
                              "precio":producto.precio,
                              "foto":producto.product_img1.url,} 
                             for producto in Producto.objects.filter(product_name = str(name_product).capitalize())]
                #try search the product for his name in lower()
                if product == []:
                    product = [{"id":producto.id, 
                              "name":producto.product_name, 
                              "description":producto.product_description, 
                              "precio":producto.precio,
                              "foto":producto.product_img1.url,} 
                             for producto in Producto.objects.filter(product_name = str(name_product).lower())]
                    if product == []:   
                        return Response(['Not Found'], status = status.HTTP_404_NOT_FOUND)
                    return Response(product, status = status.HTTP_200_OK)
                return Response(product, status = status.HTTP_200_OK) 
        except:
            return Response([], status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class Store(APIView):
    def get(self, request, category_id = None, id_product = None, page = 1):
        try:
            #return the product of the id gived
            if id_product != None:
                product = [{"id":producto.id, 
                            "name":producto.product_name, 
                            "description":producto.product_description, 
                            "about":producto.about,
                            "precio":producto.precio,
                            "fotos":[producto.product_img1.url,
                                     producto.product_img2.url,
                                     producto.product_img3.url],
                            "category_id":producto.categoria.id,
                            "category_name":producto.categoria.nombre, 
                            "updated":producto.updated_at} 
                             for producto in Producto.objects.filter(id = id_product)]
                if product == []:
                    return Response([],status = status.HTTP_404_NOT_FOUND)
                return Response(product, status = status.HTTP_200_OK)
            
            #si no recive una categoria por url devuelve todos los productos
            if category_id == None or category_id == 0: 
                productos = [{"id":producto.id, 
                              "name":producto.product_name, 
                              "description":producto.product_description, 
                              "precio":producto.precio,
                              "foto":producto.product_img1.url,} 
                             for producto in Producto.objects.all()]
                p = Paginator(productos, 24)
                return Response(p.page(page).object_list, status = status.HTTP_200_OK)
            
            #devuelve los productos que pertenecen a la categoria recivida por url
            else: 
                productos = [{"id":producto.id, 
                              "name":producto.product_name, 
                              "description":producto.product_description, 
                              "precio":producto.precio,
                              "foto":producto.product_img1.url,}
                             for producto in Producto.objects.filter(categoria = category_id)]
                if productos == []:
                    return Response([],status = status.HTTP_404_NOT_FOUND)
                else:
                    return Response(productos, status = status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
   