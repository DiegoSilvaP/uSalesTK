# Generated by Django 2.1 on 2019-03-14 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_basket', '0010_remove_shopping_basketitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_basketitem',
            name='price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8, verbose_name='Subtotal'),
        ),
    ]