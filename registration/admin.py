from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

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


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)