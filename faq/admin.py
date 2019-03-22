from django.contrib import admin
from .models import FAQ

# Register your models here.
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    readonly_fields=('created', 'updated')
    verbose_name = 'Preguntas frecuentes'

admin.site.register(FAQ, FAQAdmin)
