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

class Privacy(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200, default='Políticas de privacidad')
    content = RichTextField(verbose_name="Contenido", default='')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name='Política de privacidad'
        verbose_name_plural = 'Políticas de privacidad'
    
    def __str__(self):
        return self.title

def custom_upload_to(instance, filename):
    # 'instance' hace referencia al objeto que se esta guardando, pero despues de que se haya confirmado el nuevo valor,
    # en 'filename tendremos el nombre del fichero con la imagen que queremos sobreescribir
    old_instance = Carousel.objects.get(pk=instance.pk)
    old_instance.image.delete()
    return 'carousel/'+filename

class Carousel(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    image = models.ImageField(upload_to='Carousel', null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Imagen del carrusel"
        verbose_name_plural = "Imagenes del carrusel"
        ordering = ['title']

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(verbose_name='Pregunta', max_length=150, default='¿Es posible...?')
    answer = models.TextField(verbose_name='Respuesta', max_length=500, default='')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name='Pregunta frecuente'
        verbose_name_plural = 'Preguntas frecuentes'
    
    def __str__(self):
        return self.question