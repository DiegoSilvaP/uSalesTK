from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200, default='Quienes somos')
    content = RichTextField(verbose_name="Contenido", default='')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name='Acerca de'
        verbose_name_plural = 'Acerca de'
    
    def __str__(self):
        return self.title