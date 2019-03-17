from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import django_filters



# Para borrar la foto anterior y solo dejar la actual, vamos a sobreescribir el metodo 'upload_to'
# Dentro de esta funcionalidad, recuperaremos el antiguo avatar y lo borraremos haciendo uso del metodo 'delete'
# que tienen los 'image_field' y los 'file_field' y cuando se haya borrado, se devolvera la ruta normal a 'profiles'
def custom_upload_to(instance, filename):
    # 'instance' hace referencia al objeto que se esta guardando, pero despues de que se haya confirmado el nuevo valor,
    # en 'filename tendremos el nombre del fichero con la imagen que queremos sobreescribir
    old_instance = products.objects.get(pk=instance.pk)
    old_instance.picture.delete()
    return 'publications/'+filename


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    
    # Hay que agregar una subclase para modificar los nombres y ponerlos en español
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorías"
        # ordenamiento
        # por defecto, django ordena del más viejo al mas nuevo, por lo que se le agrega un -
        # para ordenar del mas nuevo al mas viejo
        ordering = ["name"]

    def __str__(self):
        return self.name
    

# Create your models here.
class Publication(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Vendedor", default=1)
    product = models.TextField(verbose_name="Producto", max_length=200)
    description = RichTextField(verbose_name="Descripción")
    stock = models.PositiveSmallIntegerField(verbose_name="Cantidad", default=10)
    price = models.DecimalField(verbose_name="Precio por unidad", decimal_places=1, max_digits=8, default=0)
    category = models.ForeignKey(Category, verbose_name="Categoria", related_name="get_categories", on_delete=models.CASCADE, default="")
    picture = models.ImageField(verbose_name="Imagen del encabezado", upload_to='publications', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")


    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-created', 'product']

    def __str__(self):
        return self.product


