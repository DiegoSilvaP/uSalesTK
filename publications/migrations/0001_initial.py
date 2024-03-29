# Generated by Django 2.1 on 2019-03-29 09:51

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import publications.models


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
                'ordering': ['-created', 'name'],
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
                ('picture', models.ImageField(upload_to=publications.models.custom_upload_to, verbose_name='Imagen del encabezado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('category', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='get_categories', to='publications.Category', verbose_name='Categoría')),
                ('seller', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Vendedor')),
            ],
            options={
                'verbose_name': 'publicación',
                'verbose_name_plural': 'publicaciones',
                'ordering': ['-created', 'product'],
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('parentCategory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='publications.Category', verbose_name='Categoría padre')),
            ],
            options={
                'verbose_name': 'subcategoria',
                'verbose_name_plural': 'subcategorías',
                'ordering': ['-created', '-parentCategory'],
            },
        ),
        migrations.AddField(
            model_name='publication',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='get_subcategories', to='publications.SubCategory', verbose_name='Subcategoría'),
        ),
    ]
