from django.urls import path

from location.api.views import LocationListAPIViewSet, LocationDetailAPIView

urlpatterns = [
    path('v1/location/list/', LocationListAPIViewSet.as_view(), name='location_list_api'),
    path('v1/location/<int:pk>/', LocationDetailAPIView.as_view(), name='location_detail_api'),
]
