from rest_framework import viewsets
from offers_app.models import Offer, OfferDetails
from offers_app.permissions import IsBusinessType
from rest_framework.permissions import IsAuthenticated
from .serializer import OfferSerializer, OfferDetailsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from offers_app.pagination import LargeResultsSetPagination
from rest_framework.permissions import AllowAny

class OfferDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OfferDetails.objects.all()
    serializer_class = OfferDetailsSerializer

class OfferViewSet(viewsets.ModelViewSet):
    permission_classes = [IsBusinessType, IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'description']
    ordering = ['-min_price']

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
