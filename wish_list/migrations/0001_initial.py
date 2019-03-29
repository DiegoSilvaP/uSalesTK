# Generated by Django 2.1 on 2019-03-29 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish_listItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
                ('publication', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='publications.Publication', verbose_name='Publicación')),
            ],
            options={
                'verbose_name': 'Lista de deseos',
                'verbose_name_plural': 'Listas de deseos',
            },
        ),
    ]
