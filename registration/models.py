from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Para borrar la foto anterior y solo dejar la actual, vamos a sobreescribir el metodo 'upload_to'
# Dentro de esta funcionalidad, recuperaremos el antiguo avatar y lo borraremos haciendo uso del metodo 'delete'
# que tienen los 'image_field' y los 'file_field' y cuando se haya borrado, se devolvera la ruta normal a 'profiles'
def custom_upload_to(instance, filename):
    # 'instance' hace referencia al objeto que se esta guardando, pero despues de que se haya confirmado el nuevo valor,
    # en 'filename tendremos el nombre del fichero con la imagen que queremos sobreescribir
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/'+filename
    
# Create your models here.
class Profile(models.Model):
    # Relacion 1 a 1, le indica al modelo que solo puede haber un perfil por usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.TextField(max_length=10)
    addess = models.TextField(max_length=100)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        ordering = ['user__username']

    def __str__(self):
        return self.user.username

# Introduccion a signals
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    # Comprobamos si es la primera ves que se guarda el perfil
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print('Se ha creado un usuario con su perfil enlazado')