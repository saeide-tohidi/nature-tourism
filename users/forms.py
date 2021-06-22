import random
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from .models import CustomUser
from persiantools import characters, digits


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('phoneNo',)

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data["phoneNo"] = digits.fa_to_en(cleaned_data["phoneNo"])


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('phoneNo',)
