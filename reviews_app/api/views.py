from rest_framework import viewsets
from reviews_app.models import Review
from .serializer import ReviewSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from reviews_app.permissions import IsReviewerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class CreateReviewView(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['business_user', 'reviewer']
    ordering_fields = ['updated_at', 'rating']
    ordering = ['-updated_at'] #defult

# serializer.is_valid() or serializer.save()
# DRF’s ModelViewSet already handles all of that internally for standard actions like .create(), .update(), etc.
