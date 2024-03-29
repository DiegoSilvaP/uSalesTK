# Generated by Django 2.1 on 2019-03-29 09:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=64, verbose_name='Institución bancaria')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Entidad Bancaria',
                'verbose_name_plural': 'Entidades Bancarias',
            },
        ),
        migrations.CreateModel(
            name='Plastic_money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(16), django.core.validators.MaxLengthValidator(16)], verbose_name='Número de tarjeta')),
                ('exp_month', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=3, verbose_name='Mes')),
                ('exp_year', models.IntegerField(choices=[(2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025)], default=2019, verbose_name='Año')),
                ('owner', models.CharField(max_length=32, verbose_name='Nombre del titular')),
                ('cvv', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(3)], verbose_name='Número de seguridad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('entity', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registration.Bank_entity', verbose_name='Banco')),
                ('owner_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tarjeta de crédito / débito',
                'verbose_name_plural': 'Tarjetas de crédito / débito',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.TextField(blank=True, default='', max_length=10, null=True)),
                ('address', models.TextField(blank=True, default='', max_length=100, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=registration.models.custom_upload_to)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__username'],
            },
        ),
    ]
