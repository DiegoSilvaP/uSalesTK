from django.contrib import admin
from .models import AboutUs, Privacy, Carousel, FAQ

# Register your models here.
class AboutusAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields=('created', 'updated')
    verbose_name = 'Información'
    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('publications/css/custom_ckeditor.css',)
        }

class PrivacyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields=('created', 'updated')
    verbose_name = 'Información'
    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('publications/css/custom_ckeditor.css',)
        }

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields=('created', 'updated')
    verbose_name = 'Imagenes del carrusel'

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    readonly_fields=('created', 'updated')
    verbose_name = 'Preguntas frecuentes'


admin.site.register(FAQ, FAQAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(AboutUs, AboutusAdmin)
admin.site.register(Privacy, PrivacyAdmin)