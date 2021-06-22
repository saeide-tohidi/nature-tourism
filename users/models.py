from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from users.managers import CustomUserManager
from users.validators import PhoneNoValidator
from django.utils.translation import gettext_lazy as _
from unidecode import unidecode


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    This custom user gives the ability of registering using phoneNo,
    so the username will be a user's phoneNo
    Additional Fields:
    1. user type: for determining that weather a user is a teacher
    or student or admin
    2. is_staff: is the equvilant of userType = Admin
    3. is_active: default is True
    """
    phoneNo_validator = PhoneNoValidator()
    phoneNo = models.CharField(
        _('phone number'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 15 characters or fewer. Only digits.'),
        error_messages={
            'unique': _("A user with that phone number already exists."),
        },
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    hasActivated = models.BooleanField(default=False)

    USERNAME_FIELD = 'phoneNo'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def clean(self):
        self.phoneNo = unidecode(self.phoneNo)
        # if not self.phoneNo.isdigit() or len(self.phoneNo) > 11 or len(self.phoneNo) < 11:
        #     raise ValidationError(_('شماره تماس معتبری وارد کنید!'))

    def __str__(self):
        return self.phoneNo

    class Meta:
        verbose_name = _("کاربر")
        verbose_name_plural = _("کاربران")
