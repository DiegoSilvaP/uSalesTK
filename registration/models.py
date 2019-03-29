from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.template.defaultfilters import truncatechars  # or truncatewords


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
    phone = models.TextField(max_length=10,null=True, blank=True, default='')
    address = models.TextField(max_length=100,null=True, blank=True, default='')
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        ordering = ['user__username']

    def __str__(self):
        return self.user.username


class Bank_entity(models.Model):
    bank = models.CharField(max_length=64, verbose_name='Institución bancaria')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name='Entidad Bancaria'
        verbose_name_plural='Entidades Bancarias'
        
    def __str__(self):
        return self.bank

YEAR_CHOICES = []
for r in range(datetime.datetime.now().year, (datetime.datetime.now().year+7)):
    YEAR_CHOICES.append((r,r))

MONTH_CHOICES = []
for r in range(1, 13):
    MONTH_CHOICES.append((r,r))

TYPECARD_CHOICES = (
        (1, 'Crédito'),
        (2, 'Débito'),
    )

class Plastic_money(models.Model):
    entity = models.ForeignKey(Bank_entity, on_delete=models.CASCADE, verbose_name='Banco', default=1)
    # type_card = models.IntegerField(verbose_name='Tipo', choices=TYPECARD_CHOICES, default=1)
    card_number = models.CharField(validators=[
            MinLengthValidator(16),
            MaxLengthValidator(16)
        ], max_length=16, verbose_name='Número de tarjeta')
    exp_month = models.IntegerField(verbose_name='Mes', choices=MONTH_CHOICES, default=datetime.datetime.now().month)
    exp_year = models.IntegerField(verbose_name='Año', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    owner_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.CharField(verbose_name='Nombre del titular', max_length=32)
    cvv = models.CharField(validators=[
            MinLengthValidator(3),
            MaxLengthValidator(3)
        ], max_length=3, verbose_name='Número de seguridad')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Tarjeta de crédito / débito'
        verbose_name_plural = 'Tarjetas de crédito / débito'
        ordering=[('-created')]

    @property
    def short_cardNumber(self):
        return truncatechars(self.card_number, 7)

    def __str__(self):
        return self.card_number


# Introduccion a signals
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    # Comprobamos si es la primera ves que se guarda el perfil
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print('Se ha creado un usuario con su perfil enlazado')

