from rest_framework import viewsets
from reviews_app.models import Review
from .serializer import ReviewSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from reviews_app.permissions import IsReviewerOrReadOnly


class CreateReviewView(ModelViewSet):
    permission_classes = [IsReviewerOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# serializer.is_valid() or serializer.save()
# DRF’s ModelViewSet already handles all of that internally for standard actions like .create(), .update(), etc.