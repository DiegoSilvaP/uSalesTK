# Generated by Django 2.1 on 2019-03-22 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'Pregunta frecuente', 'verbose_name_plural': 'Preguntas frecuentes'},
        ),
    ]