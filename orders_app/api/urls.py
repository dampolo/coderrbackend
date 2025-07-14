from rest_framework.routers import DefaultRouter
from .views import OrderCreateFromOfferView
from django.urls import path, include

router = DefaultRouter()
router.register(r'orders', OrderCreateFromOfferView, basename='orders' )

urlpatterns = [
    path('', include(router.urls)),
]
