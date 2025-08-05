from rest_framework import viewsets
from offers_app.models import Offer, OfferDetails
from offers_app.permissions import IsBusinessType
from rest_framework.permissions import IsAuthenticated
from .serializer import OfferSerializer, OfferDetailsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from offers_app.pagination import LargeResultsSetPagination
from rest_framework.permissions import AllowAny
import django_filters

class OfferDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OfferDetails.objects.all()
    serializer_class = OfferDetailsSerializer

class OfferFilter(django_filters.FilterSet):
    # Matches offers with price >= this value
    min_price = django_filters.NumberFilter(field_name='min_price', lookup_expr='gte')
    
    # Matches offers where delivery time is <= this value
    max_delivery_time = django_filters.NumberFilter(field_name='min_delivery_time', lookup_expr='lte')

    class Meta:
        model = Offer
        fields = ['min_price', 'max_delivery_time']

class OfferViewSet(viewsets.ModelViewSet):
    permission_classes = [IsBusinessType]
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'description']
    ordering = ['min_price', '-updated_at', 'min_delivery_time']
    filterset_class = OfferFilter
    
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
