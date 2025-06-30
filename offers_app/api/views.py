from rest_framework import viewsets
from offers_app.models import Offer
from .serializer import OfferSerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
