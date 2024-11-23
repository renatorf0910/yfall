from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'name', 'cpf', 'age', 'phone', 'is_active', 'is_super')
    list_filter = ('is_super', 'is_active')
    search_fields = ('username', 'email', 'cpf', 'phone')
    ordering = ('username',)

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Informações Pessoais', {
            'fields': ('username', 'name', 'age', 'cpf', 'address', 'phone')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_super', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'name', 'cpf', 'age', 'phone', 'is_active', 'password1', 'password2')
        }),
    )

admin.site.register(User, CustomUserAdmin)
