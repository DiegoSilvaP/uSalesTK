from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Bank_entity, Plastic_money


# Register your models here.
class ProfileAdmin(admin.StackedInline):
    model = Profile
    verbose_name='Perfil'
    verbose_name_plural = 'Perfiles'
    fk_name = 'user'
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileAdmin, )
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class BankEntityAdmin(admin.ModelAdmin):
    list_display = ('bank','created',)
    readonly_fields=('created', 'updated')
    verbose_name = 'Entidad bancaria'



class PlasticMoneyAdmin(admin.ModelAdmin):
    list_display = ('entity','owner','short_cardNumber')
    readonly_fields=('created', 'updated')
    verbose_name = 'Tarjeta de crédito / débito'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Bank_entity, BankEntityAdmin)
admin.site.register(Plastic_money, PlasticMoneyAdmin)