from django.contrib import admin
from .models import Orders

# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('folio','customer','product','payment_status','shipping_status','quantity','subtotal', 'created', 'updated')
    readonly_fields=('folio','customer','product','quantity','subtotal', 'created', 'updated')
    verbose_name = 'Compra'


admin.site.register(Orders, OrdersAdmin)
