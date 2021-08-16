from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    title = models.CharField(_("عنوان"), max_length=50, null=True, blank=True)
    ostan = models.CharField(_("استان"), max_length=50, null=True, blank=True)
    shahr = models.CharField(_("شهر"), max_length=50, null=True, blank=True)
    address = models.TextField(_("آدرس"), null=True, blank=True)
    desc = models.TextField(_("توضیحات"), null=True, blank=True)
    approved = models.BooleanField(_("تایید شده"), default=True)
    created_at = models.DateTimeField(_("ایجاد شده در"), auto_now_add=True)
    update_at = models.DateTimeField(_("ایجاد شده در"), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("مکان")
        verbose_name_plural = _("مکان‌‌ها")
