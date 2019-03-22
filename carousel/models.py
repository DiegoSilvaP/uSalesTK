from django.db import models

# Create your models here.

def custom_upload_to(instance, filename):
    # 'instance' hace referencia al objeto que se esta guardando, pero despues de que se haya confirmado el nuevo valor,
    # en 'filename tendremos el nombre del fichero con la imagen que queremos sobreescribir
    old_instance = Carousel.objects.get(pk=instance.pk)
    old_instance.image.delete()
    return 'Carousel/'+filename

class Carousel(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    image = models.ImageField(upload_to='Carousel', null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Imagen del carrusel"
        verbose_name_plural = "Imagenes del carrusel"
        ordering = ['-title']

    def __str__(self):
        return self.title