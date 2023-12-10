from django.db import models

class Promo(models.Model):
    name = models.CharField(max_length=50, verbose_name = "Nombre")
    description = models.CharField(max_length=50, verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "promos")
    product1 = models.CharField(max_length=100, verbose_name = "Producto1")
    product2 = models.CharField(max_length=100, verbose_name = "Producto2")
    product3 = models.CharField(max_length=100, verbose_name = "Producto3")
    product4 = models.CharField(max_length=100, verbose_name = "Producto4")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha modificación")
    position = models.IntegerField(verbose_name="Posición de la imagen", default=1)
    
    class Meta:
        verbose_name = "Promo"
        verbose_name_plural = "Promos"
        ordering = ['created']
        
    def __str__(self):
        return self.name