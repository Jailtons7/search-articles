from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from authentication.forms import AddUserForm, EditUserForm
from authentication.models import SearchGroup, SearchPermission

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = AddUserForm
    form = EditUserForm
    model = User
    list_display = ('email', 'cpf', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'is_trusty')
    search_fields = ('email', 'cpf', 'first_name', 'last_name',)
    ordering = ('email', 'first_name', 'last_name',)
    fieldsets = (
        (None, {'fields': (
            'email', 'cpf', 'first_name', 'last_name', 'password',
            'is_superuser', 'is_trusty'
        )}),
        ('Permissions', {
            'classes': ('collapse',),
            'fields': ('is_staff', 'is_active')
        }),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('user_permissions', 'groups')
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'cpf', 'first_name', 'last_name', 'password', 'password2',
                'is_staff', 'is_active', 'is_superuser', 'is_trusty'
            )
        }),
    )


@admin.register(SearchGroup)
class RedeGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(SearchPermission)
class RedePermissionsAdmin(admin.ModelAdmin):
    pass
