from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length= 255)
    
    class Meta:
        ordering = ["id"]
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    precio = models.FloatField(default = 0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    product_img1 = models.ImageField(upload_to = "productos_images", default = "productos_images/blank.png")
    product_img2 = models.ImageField(upload_to = "productos_images", default = "productos_images/blank.png")
    product_img3 = models.ImageField(upload_to = "productos_images", default = "productos_images/blank.png")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ["id"]
    
    def __str__(self):
        return self.product_name
    
    
