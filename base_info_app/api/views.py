from rest_framework.views import APIView
from rest_framework.response import Response
from reviews_app .models import Review
from django.db.models import Avg
from auth_app.models import Profile
from offers_app.models import Offer


class BaseInfoView(APIView):
      def get(self, request):
        review_count = Review.objects.count()
        average_rating = Review.objects.aggregate(Avg("rating", default=0))["rating__avg"]
        business_profile_count = Profile.objects.filter(type="customer").count()
        offer_count = Offer.objects.count()

        return Response({
            "review_count": review_count,
            "average_rating": average_rating,
            "business_profile_count": business_profile_count,
            "offer_count": offer_count
        })