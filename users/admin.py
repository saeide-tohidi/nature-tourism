from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    fields = ('first_name', 'last_name', 'picture', 'gender', 'email',)
    readonly_fields = ['creation_date']
    extra = False
    can_delete = False


class CustomUserAdmin(UserAdmin):
    """
    This activation will give the admin the ability of modifying
    users and there status and also there activation status
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('get_full_name', 'phoneNo', 'is_staff', 'is_active', 'hasActivated')
    list_filter = ('phoneNo', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('phoneNo', 'password')}),
        ('Permissions', {'fields': (
            'is_staff', 'is_active', 'hasActivated', 'groups')}),
    )
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': (
        'phoneNo', 'password1', 'password2', 'is_staff', 'is_active', 'hasActivated',)}),)

    inlines = [UserProfileInline, ]

    def get_full_name(self, obj):
        return obj.profile.full_name

    get_full_name.short_description = "کاربر"
    search_fields = ('profile__first_name', 'profile__last_name', 'phoneNo',)
    ordering = ('-id',)


admin.site.register(CustomUser, CustomUserAdmin)
