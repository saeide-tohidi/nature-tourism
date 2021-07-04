from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from users.managers import CustomUserManager
from users.validators import PhoneNoValidator
from django.utils.translation import gettext_lazy as _
from unidecode import unidecode
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


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


class UserProfile(models.Model):
    """
       Stores a user entry, related to :model:`users.CustomUser`.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, verbose_name=_(
        'کاربر'), on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(_('نام'), max_length=40, default='طبیعت‌گرد')
    last_name = models.CharField(_('نام خانوادگی'), max_length=40, default='0')
    picture = models.ImageField(_('تصویر'), blank=True, null=True)
    GENDERS = [
        ('M', _('مرد')),
        ('F', _('زن')),
    ]
    gender = models.CharField(_('جنسیت'), max_length=1, choices=GENDERS, default='F')
    email = models.CharField(_('ایمیل'), max_length=100, blank=True, null=True)
    creation_date = models.DateTimeField(_('تاریخ ایجاد'), auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name}  {self.last_name}"

    class Meta:
        db_table = "user_profile"
        verbose_name = _("پروفایل کاربر")
        verbose_name_plural = _("پروفایل کاربران")
