from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from users.forms import CustomUserChangeFormInAdmin, CustomUserRegistrationForm
from users.models import CustomUserModel


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeFormInAdmin
    add_form = CustomUserRegistrationForm

    list_display = (
        'phone', 'name', 'get_full_name', 'birthday', 'photo',
        'registration_date', 'is_active', 'is_staff', 'is_superuser', 'is_verified', 'slug'
    )
    list_display_links = (
        'phone',
        'name',
        'slug',
    )
    list_filter = (
        'is_staff',
        'is_verified',
    )
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'birthday', 'photo')}),
        (_('Personal info'), {'fields': ('phone', 'name', 'slug')}),
        (_('Permission'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Verification'), {'fields': ('verified_code', 'is_verified')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'name', 'password1', 'password2'),
        }),
    )
    search_fields = (
        'phone',
        'name',
    )
    ordering = (
        'name',
    )
    filter_horizontal = (

    )


admin.site.register(CustomUserModel, CustomUserAdmin)
admin.site.unregister(Group)
