from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id","nombre")
    list_filter = ("nombre",)
    search_fields = ("nombre",)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id","product_name","precio","categoria", "product_img", "updated_at")
    list_filter = ("product_name","categoria",)
    search_fields = ("product_name",)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
