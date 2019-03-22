from django.contrib import admin
from .models import Privacy

# Register your models here.
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields=('created', 'updated')
    verbose_name = 'Politicas de privacidad'
    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('publications/css/custom_ckeditor.css',)
        }

admin.site.register(Privacy, PrivacyAdmin)