from django.contrib import admin
from .models import Publication, Category

# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('seller','product',  'price', 'stock', 'created', 'updated')
    readonly_fields=('created', 'updated')
    verbose_name = 'Publicación'

    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('publications/css/custom_ckeditor.css',)
        }

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Publication, PublicationAdmin)
admin.site.register(Category, CategoryAdmin)
