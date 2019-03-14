# Generated by Django 2.1 on 2019-03-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1500.5, max_digits=8, verbose_name='Precio por unidad'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='stock',
            field=models.SmallIntegerField(default=10, verbose_name='Cantidad'),
        ),
    ]
