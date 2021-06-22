from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where phoneNo is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, phoneNo, password, **extraFields):
        """
        Create and save a User with the given phoneNo, password
        """
        if not phoneNo:
            raise ValueError(_('The Phone Number must be set'))
        phoneNo = self.normilize_phone_no(phoneNo)
        user = self.model(phoneNo=phoneNo, **extraFields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phoneNo, password, **extraFields):
        """
        Create and save a SuperUser with the given phoneNo and password.
        """
        extraFields.setdefault('is_staff', True)
        extraFields.setdefault('is_superuser', True)
        extraFields.setdefault('is_active', True)

        if extraFields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extraFields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phoneNo, password, **extraFields)

    def normilize_phone_no(self, phoneNo):
        # TODO -> Fix this function and add more checks
        return phoneNo
