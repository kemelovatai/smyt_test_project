from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from auth_user import models


admin.site.unregister(Group)


@admin.register(models.User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'full_name', 'is_superuser', 'is_staff')
    readonly_fields = ('created_at', 'updated_at', 'last_login')
    fieldsets = (
        (_('Main info'), {'fields': ('full_name', 'email', 'password')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff', 'user_permissions')}),
        (_('Important dates'), {'fields': ('created_at', 'updated_at', 'last_login')}),
    )
    add_fieldsets = (
        (_('Main info'), {'fields': ('full_name', 'email', 'password1', 'password2')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff', 'user_permissions')}),
    )
    list_filter = ('is_superuser', 'is_staff')
    search_fields = ('email', 'full_name')
    ordering = ('-created_at',)
