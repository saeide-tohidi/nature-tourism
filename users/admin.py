from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    This activation will give the admin the ability of modifying
    users and there status and also there activation status
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('phoneNo', 'is_staff', 'is_active', 'hasActivated')
    list_filter = ('phoneNo', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('phoneNo', 'password')}),
        ('Permissions', {'fields': (
            'is_staff', 'is_active', 'hasActivated',   'groups')}),
    )
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': (
        'phoneNo', 'password1', 'password2', 'is_staff', 'is_active', 'hasActivated',)}),)
    ordering = ('id',)

admin.site.register(CustomUser, CustomUserAdmin)
