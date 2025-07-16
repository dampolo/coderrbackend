from rest_framework import serializers
from reviews_app.models import Review
from django.shortcuts import get_object_or_404

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.SerializerMethodField(read_only=True)
    # print(reviewer)
    class Meta:
        model = Review
        fields = [
            "id",
            "business_user",
            "reviewer",
            "rating",
            "description",
            "created_at",
            "updated_at"
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "reviewer"
        ]

    def get_reviewer(self, obj):
        return {
            "id": obj.reviewer.id
        }