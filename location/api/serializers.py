from rest_framework import serializers
from location.models import Location


class LocationListSerializer(serializers.ModelSerializer):
    location_url = serializers.HyperlinkedIdentityField(view_name='location_detail_api')

    class Meta:
        model = Location
        fields = [
            'location_url',
            'title',
            'ostan',
        ]


class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
