from django.db import models
from publications.models import Publication
from django.contrib.auth.models import User 

# Create your models here.
class Wish_listItem(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Cliente", default=1)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE,verbose_name="Publicación", default=1)