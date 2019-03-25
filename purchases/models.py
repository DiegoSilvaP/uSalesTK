from django.db import models
from django.contrib.auth.models import User
from publications.models import Publication
# Create your models here.
class Purchase(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Cliente", default=1)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE,verbose_name="Publicación", default=1)
    quantity = models.PositiveSmallIntegerField(verbose_name="Cantidad", default=1)
    price = models.DecimalField(verbose_name="Subtotal", decimal_places=1, max_digits=8, default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")
