from django.db import models
from publications.models import Publication
from django.contrib.auth.models import User 
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Shopping_basketItem(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Cliente", default=1)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE,verbose_name="Publicación", default=1)
    quantity = models.PositiveSmallIntegerField(verbose_name="Cantidad", default=1)
    price = models.DecimalField(verbose_name="Subtotal", decimal_places=1, max_digits=8, default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Carrito de compras"
        verbose_name_plural = "Carritos de compras"
    
    def __str__(self):
        return self.publication.product