from django.contrib import admin
from .models import AboutUs

# Register your models here.
class InformationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields=('created', 'updated')
    verbose_name = 'Información'
    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('publications/css/custom_ckeditor.css',)
        }

admin.site.register(AboutUs, InformationAdmin)