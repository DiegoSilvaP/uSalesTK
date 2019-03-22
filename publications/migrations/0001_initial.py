# Generated by Django 2.1 on 2019-03-21 06:42

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorías',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField(max_length=200, verbose_name='Producto')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripción')),
                ('stock', models.PositiveSmallIntegerField(default=10, verbose_name='Cantidad')),
                ('price', models.DecimalField(decimal_places=1, default=0, max_digits=8, verbose_name='Precio por unidad')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='publications', verbose_name='Imagen del encabezado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='get_categories', to='publications.Category', verbose_name='Categoria')),
                ('seller', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Vendedor')),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
                'ordering': ['-created', 'product'],
            },
        ),
    ]
