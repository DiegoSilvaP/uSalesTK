from django.db import models

# Create your models here.
class FAQ(models.Model):
    question = models.CharField(verbose_name='Pregunta', max_length=150, default='¿Es posible...?')
    answer = models.TextField(verbose_name='Respuesta', max_length=500, default='')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name='Pregunta frecuente'
        verbose_name_plural = 'Preguntas frecuentes'
    
    def __str__(self):
        return self.question