from django.db import models
from publications.models import Publication
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.
class Wish_listItem(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Cliente", default=1)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE,verbose_name="Publicación", default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")


    class Meta:
        verbose_name = "Lista de deseos"
        verbose_name_plural = "Listas de deseos"