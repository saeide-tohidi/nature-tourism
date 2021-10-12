from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField


class TravelType(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL, verbose_name='دسته‌مادر')
    title_P = models.CharField(max_length=50, verbose_name='عنوان فارسی')
    title_E = models.CharField(max_length=50, verbose_name='عنوان انگلیسی')
    image = models.ImageField(blank=True, null=True, verbose_name='تصویر')
    created_at = models.DateTimeField(_("ایجاد شده در"), auto_now_add=True)
    update_at = models.DateTimeField(_("ایجاد شده در"), auto_now=True)

    def __str__(self):
        return self.title_P

    class MPTTMeta:
        order_insertion_by = ['title_E']

    class Meta:
        verbose_name = 'نوع سفر'
        verbose_name_plural = 'انواع سفر'


class TransportType(models.Model):
    title_P = models.CharField(max_length=50, verbose_name='عنوان فارسی')
    title_E = models.CharField(max_length=50, verbose_name='عنوان انگلیسی')
    image = models.ImageField(blank=True, null=True, verbose_name='تصویر')
    created_at = models.DateTimeField(_("ایجاد شده در"), auto_now_add=True)
    update_at = models.DateTimeField(_("ایجاد شده در"), auto_now=True)

    def __str__(self):
        return self.title_P

    class Meta:
        verbose_name = 'نوع حمل و نقل'
        verbose_name_plural = 'نوع حمل و نقل'


class TravelTime(models.Model):
    title_P = models.CharField(max_length=50, verbose_name='عنوان فارسی')
    title_E = models.CharField(max_length=50, verbose_name='عنوان انگلیسی')
    image = models.ImageField(blank=True, null=True, verbose_name='تصویر')
    created_at = models.DateTimeField(_("ایجاد شده در"), auto_now_add=True)
    update_at = models.DateTimeField(_("ایجاد شده در"), auto_now=True)

    def __str__(self):
        return self.title_P

    class Meta:
        verbose_name = 'مدت زمان سفر'
        verbose_name_plural = 'مدت زمان سفر'


class Difficulty(models.Model):
    title_P = models.CharField(max_length=50, verbose_name='عنوان فارسی')
    title_E = models.CharField(max_length=50, verbose_name='عنوان انگلیسی')
    image = models.ImageField(blank=True, null=True, verbose_name='تصویر')
    created_at = models.DateTimeField(_("ایجاد شده در"), auto_now_add=True)
    update_at = models.DateTimeField(_("ایجاد شده در"), auto_now=True)

    def __str__(self):
        return self.title_P

    class Meta:
        verbose_name = 'سطح سختی سفر'
        verbose_name_plural = 'سطح سختی سفر'


class Location(models.Model):
    title = models.CharField(_("عنوان"), max_length=50, null=True, blank=True)
    travel_type = models.ManyToManyField("location.TravelType", related_name='loc_travel', verbose_name=_("نوع سفر"))
    transport_type = models.ManyToManyField("location.TransportType",related_name='loc_transport', verbose_name=_("نوع حمل و نقل"))
    travel_time = models.ManyToManyField("location.TravelTime", related_name='loc_time', verbose_name=_("زمانبندی"))
    difficulty = models.ManyToManyField("location.Difficulty", related_name='loc_difficulty', verbose_name=_("درجه سختی"))
    ostan = models.CharField(_("استان"), max_length=50, null=True, blank=True)
    shahr = models.CharField(_("شهر"), max_length=50, null=True, blank=True)
    address = models.TextField(_("آدرس"), null=True, blank=True)
    desc = RichTextField(_("توضیحات"), null=True, blank=True)
    approved = models.BooleanField(_("تایید شده"), default=True)
    created_at = models.DateTimeField(_("ایجاد شده در"), auto_now_add=True)
    update_at = models.DateTimeField(_("ایجاد شده در"), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("مکان")
        verbose_name_plural = _("مکان‌‌ها")
