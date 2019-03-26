from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import django_filters
from django.dispatch import receiver
from django.db.models.signals import post_save



# Para borrar la foto anterior y solo dejar la actual, vamos a sobreescribir el metodo 'upload_to'
# Dentro de esta funcionalidad, recuperaremos el antiguo avatar y lo borraremos haciendo uso del metodo 'delete'
# que tienen los 'image_field' y los 'file_field' y cuando se haya borrado, se devolvera la ruta normal a 'profiles'
def custom_upload_to(instance, filename):
    # 'instance' hace referencia al objeto que se esta guardando, pero despues de que se haya confirmado el nuevo valor,
    # en 'filename tendremos el nombre del fichero con la imagen que queremos sobreescribir
    if instance.pk == None:
        return 'publications/'+filename
    else:
        old_instance = Publication.objects.get(pk=instance.pk)
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
        ordering = ['-created', 'name']
    
    # Set 2 computed properties on the model which can be accessed from the template

    def get_subcategories(self):
      return SubCategory.objects.filter(parentCategory=self)

    def get_subcategory_count(self):
      return SubCategory.objects.filter(parentCategory=self).count()

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    parentCategory = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoría padre", default=1)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    # Hay que agregar una subclase para modificar los nombres y ponerlos en español
    class Meta:
        verbose_name = "subcategoria"
        verbose_name_plural = "subcategorías"
        # ordenamiento
        ordering = ['-created', '-parentCategory']
        
    def __str__(self):
        return self.name

# Create your models here.
class Publication(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Vendedor", default=2)
    product = models.TextField(verbose_name="Producto", max_length=200)
    description = RichTextField(verbose_name="Descripción")
    stock = models.PositiveSmallIntegerField(verbose_name="Cantidad", default=10)
    price = models.DecimalField(verbose_name="Precio por unidad", decimal_places=1, max_digits=8, default=0)
    category = models.ForeignKey(Category, verbose_name="Categoría", related_name="get_categories", on_delete=models.SET_NULL, blank=True, null=True, default="")
    subcategory = models.ForeignKey(SubCategory, verbose_name="Subcategoría", related_name="get_subcategories", on_delete=models.SET_NULL, blank=True, null=True)
    picture = models.ImageField(verbose_name="Imagen del encabezado", upload_to=custom_upload_to)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")


    class Meta:
        verbose_name = "publicación"
        verbose_name_plural = "publicaciones"
        ordering = ['-created', 'product']

    def __str__(self):
        return self.product


