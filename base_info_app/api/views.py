from rest_framework.views import APIView
from rest_framework.response import Response
from reviews_app .models import Review
from django.db.models import Avg
from auth_app.models import Profile
from offers_app.models import Offer


class BaseInfoView(APIView):
      def get(self, request):
        return Response({
            "review_count": Review.objects.count(),
            "average_rating": Review.objects.aggregate(Avg("rating", default=0))["rating__avg"],
            "business_profile_count": Profile.objects.filter(type="business").count(),
            "offer_count": Offer.objects.count()
        })