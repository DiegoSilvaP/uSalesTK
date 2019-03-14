# Generated by Django 2.1 on 2019-03-14 01:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_basket', '0006_auto_20190313_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping_basketitem',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Cantidad'),
        ),
    ]