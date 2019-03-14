from django.contrib import admin
from .models import Shopping_basketItem
from publications.models import Publication

# Register your models here.
class Shopping_basketAdmin(admin.ModelAdmin):
    list_display = ('customer','publication', 'quantity',)
    readonly_fields=('created', 'updated')
    verbose_name = 'Carrito de compra'

admin.site.register(Shopping_basketItem, Shopping_basketAdmin)