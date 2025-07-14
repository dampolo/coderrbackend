from rest_framework.routers import DefaultRouter
from .views import OrderCreateFromOfferView, OrderCountView
from django.urls import path, include

router = DefaultRouter()
router.register(r'orders', OrderCreateFromOfferView, basename='orders' )

urlpatterns = [
    path('', include(router.urls)),
    path('order-count/<int:business_user_id>/', OrderCountView.as_view(), name='order-count')
]
