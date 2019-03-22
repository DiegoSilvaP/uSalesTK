from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Privacy(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200, default='Política de privacidad')
    content = RichTextField(verbose_name="Contenido", default='')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name='Política de privacidad'
        verbose_name_plural = 'Políticas de privacidad'
    
    def __str__(self):
        return self.title