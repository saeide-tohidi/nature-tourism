from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import generics, permissions

from location.api.filter import LocationFilter
from location.api.serializers import LocationListSerializer, LocationDetailSerializer
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from django_filters import rest_framework as filters

from location.models import Location


class LocationPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 500
    limit_query_param = "limit"
    offset_query_param = "offset"


class LocationListAPIViewSet(generics.ListAPIView):
    serializer_class = LocationListSerializer
    queryset = Location.objects.filter(approved=True)
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    pagination_class = LocationPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LocationFilter


class LocationDetailAPIView(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationDetailSerializer
    # authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        location = self.get_object()
        serializer = self.get_serializer(location)
        return Response(serializer.data)
