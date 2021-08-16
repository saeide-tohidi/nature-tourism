import django_filters
from django_filters import filters

from location.models import Location


class LocationFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='عنوان')
    ostan = django_filters.CharFilter(lookup_expr='icontains', label='استان')
    shahr = django_filters.CharFilter(lookup_expr='icontains', label='شهر')

    class Meta:
        model = Location
        fields = ['title', 'ostan', 'shahr']
