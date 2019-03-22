from django.contrib import admin
from .models import Carousel

# Register your models here.
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields=('created', 'updated')
    verbose_name = 'Imagenes del carrusel'


admin.site.register(Carousel, CarouselAdmin)