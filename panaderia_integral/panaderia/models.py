from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name = "Nombre")
    
    class Meta: 
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name = "Nombre")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "productos")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha modificación")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Categoría')

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['created']
        
    def __str__(self):
        return self.name