from rest_framework import viewsets
from offers_app.models import Offer, OfferDetails
from .serializer import OfferSerializer, OfferDetailsSerializer
from rest_framework.pagination import PageNumberPagination

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000

class OfferDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OfferDetails.objects.all()
    serializer_class = OfferDetailsSerializer

class OfferViewSet(viewsets.ModelViewSet):
    pagination_class = LargeResultsSetPagination

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
