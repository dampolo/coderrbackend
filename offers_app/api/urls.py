from rest_framework.routers import DefaultRouter 
from .views import OfferViewSet, OfferDetailsViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'offers', OfferViewSet, basename='offers')
router.register(r'offerdetails', OfferDetailsViewSet, basename='offerdetails')

urlpatterns = [
    path('', include(router.urls))
]