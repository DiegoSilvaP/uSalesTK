# Generated by Django 2.1 on 2019-03-14 00:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_basket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_basketitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Creado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopping_basketitem',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Actualizado'),
        ),
    ]