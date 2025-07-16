from rest_framework.routers import DefaultRouter
from .views import CreateReviewView
from django.urls import path, include

router = DefaultRouter()
router.register(r'reviews', CreateReviewView, basename='reviews' )

urlpatterns = [
    path('', include(router.urls)),
]
