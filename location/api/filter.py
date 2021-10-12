import django_filters
from django_filters import filters

from location.models import Location, TravelType, TravelTime, TransportType, Difficulty


class CustomField(django_filters.fields.ModelMultipleChoiceField):
    def _check_values(self, value):
        """
        Override the base class' _check_values method so our queryset is not
        empty if one of the items in value is invalid.
        """
        null = self.null_label is not None and value and self.null_value in value
        if null:
            value = [v for v in value if v != self.null_value]
        field_name = self.to_field_name or 'pk'
        result = list(self.queryset.filter(**{'{}__in'.format(field_name): value}))
        result += [self.null_value] if null else []
        return result


class CustomModelMultipleChoiceFilter(django_filters.ModelMultipleChoiceFilter):
    field_class = CustomField


class CustomField_cat(django_filters.fields.ModelMultipleChoiceField):
    def _check_values(self, value):
        """
        Override the base class' _check_values method so our queryset is not
        empty if one of the items in value is invalid.
        """
        null = self.null_label is not None and value and self.null_value in value
        if null:
            value = [v for v in value if v != self.null_value]
        field_name = self.to_field_name or 'pk'
        result = list(self.queryset.filter(**{'{}__in'.format(field_name): value}) \
                      .get_descendants(include_self=True))
        result += [self.null_value] if null else []
        return result


class CustomModelMultipleChoiceFilter_cat(django_filters.ModelMultipleChoiceFilter):
    field_class = CustomField_cat


class LocationFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='عنوان')
    ostan = django_filters.CharFilter(lookup_expr='icontains', label='استان')
    shahr = django_filters.CharFilter(lookup_expr='icontains', label='شهر')

    travel_type = CustomModelMultipleChoiceFilter_cat(field_name='travel_type__id',
                                                      to_field_name='id',
                                                      queryset=TravelType.objects.all(),
                                                      conjoined=False, )

    transport_type = CustomModelMultipleChoiceFilter(field_name='transport_type__id',
                                                     to_field_name='id',
                                                     queryset=TransportType.objects.all(),
                                                     conjoined=False, )

    travel_time = CustomModelMultipleChoiceFilter(field_name='travel_time__id',
                                                  to_field_name='id',
                                                  queryset=TravelTime.objects.all(),
                                                  conjoined=False, )

    difficulty = CustomModelMultipleChoiceFilter(field_name='difficulty__id',
                                                 to_field_name='id',
                                                 queryset=Difficulty.objects.all(),
                                                 conjoined=False, )

    class Meta:
        model = Location
        fields = ['title', 'ostan', 'shahr', 'travel_type', 'travel_time', 'difficulty', 'transport_type']
