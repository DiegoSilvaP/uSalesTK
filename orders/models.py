from django.db import models
from django.contrib.auth.models import User
from publications.models import Publication
# Create your models here.
class Orders(models.Model):
    PAYMENT_CHOICES = (
        (1, 'Pago pendiente'),
        (2, 'Pagado'),
    )

    SHIPPING_CHOICES = (
        (1, 'Envío pendiente'),
        (2, 'Enviado'),
        (3, 'Recibido'),
    )

    folio = models.CharField(verbose_name='Folio', max_length=16)
    customer = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Cliente", default=1)
    product = models.ForeignKey(Publication, on_delete=models.CASCADE,verbose_name="Publicación", default=1)
    quantity = models.PositiveSmallIntegerField(verbose_name="Cantidad", default=1)
    subtotal = models.DecimalField(verbose_name="Subtotal", decimal_places=1, max_digits=8, default=0)
    payment_status = models.IntegerField(verbose_name='Estado del pago', choices=PAYMENT_CHOICES, default=1)
    shipping_status = models.IntegerField(verbose_name='Estado del envío', choices=SHIPPING_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['created','updated','subtotal']

    def __str__(self):
        return self.product.product