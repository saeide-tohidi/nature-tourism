import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class PhoneNoValidator(validators.RegexValidator):
    regex = r'^(?:00989?|09)\d{9}'
    message = _(
        'Enter a valid phone number. This value may contain only digits, '
        'follow this pattern: 09171112234'
    )
    flags = 0
