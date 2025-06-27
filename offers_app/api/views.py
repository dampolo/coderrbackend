from rest_framework import viewsets
from offers_app.models import Offer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
