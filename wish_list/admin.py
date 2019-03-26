from django.contrib import admin
from .models import Wish_listItem

# Register your models here.
class Wish_listAdmin(admin.ModelAdmin):
    exclude=('customer',)
    list_display = ('customer','publication')
    readonly_fields=('created', 'updated')
    verbose_name = 'Lista de deseos'

admin.site.register(Wish_listItem, Wish_listAdmin)