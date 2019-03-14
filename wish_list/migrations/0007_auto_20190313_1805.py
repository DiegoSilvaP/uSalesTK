# Generated by Django 2.1 on 2019-03-14 00:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0006_auto_20190308_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish_listitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Creado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wish_listitem',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Actualizado'),
        ),
    ]
