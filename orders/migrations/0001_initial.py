# Generated by Django 2.1 on 2019-03-29 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publications', '0001_initial'),
        ('registration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(max_length=16, verbose_name='Folio')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Cantidad')),
                ('subtotal', models.DecimalField(decimal_places=1, default=0, max_digits=8, verbose_name='Subtotal')),
                ('payment_status', models.IntegerField(choices=[(1, 'Pago pendiente'), (2, 'Pagado')], default=1, verbose_name='Estado del pago')),
                ('shipping_status', models.IntegerField(choices=[(1, 'Envío pendiente'), (2, 'Enviado'), (3, 'Recibido')], default=1, verbose_name='Estado del envío')),
                ('shipping_tracker', models.CharField(blank=True, max_length=32, null=True, verbose_name='Número de seguimiento')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
                ('payment_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Plastic_money', verbose_name='Método de pago')),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='publications.Publication', verbose_name='Publicación')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['created', 'updated', 'subtotal'],
            },
        ),
    ]
