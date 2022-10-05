from django.contrib import admin
from .models import Categoria, Producto, Video

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id","nombre")
    list_filter = ("nombre",)
    search_fields = ("nombre",)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id","product_name","precio","categoria", "product_img1", "product_img2", "product_img3", "updated_at")
    list_filter = ("product_name","categoria",)
    search_fields = ("product_name",)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("id","video")

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Video, VideoAdmin)

