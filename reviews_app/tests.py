from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from auth_app.models import Profile
from reviews_app.models import Review
from reviews_app.api.serializer import ReviewSerializer
from rest_framework.exceptions import ValidationError


#Integration Tests
class ReviewsTests(APITestCase):

    def setUp(self):
        # Create customer user
        self.user = Profile.objects.create_user(
            username='testuser',
            password='pass123',
            email='test@example.com',
            type='customer'
        )

        # Create business user
        self.business_user = Profile.objects.create_user(
            username='bizuser',
            password='pass123',
            email='biz@example.com',
            type='business'
        )

        self.review = Review.objects.create(business_user=self.business_user, reviewer=self.user, rating=5, description="Alles Top" )

        # Token auth
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_list_post_review(self):

        # New business user for this test OTHERWISE you receive error "You have already reviewed this user."
        other_business = Profile.objects.create_user(
            username='newbiz',
            password='pass123',
            email='newbiz@example.com',
            type='business'
        )

        url = reverse('reviews-list')
        data = {
                'business_user': other_business.id,
                'rating': 5, 
                'description': 'Alles Top' }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_review_all_url(self):
        url = reverse('reviews-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_review_detail(self):
        url = reverse('reviews-detail', kwargs={'pk': self.review.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_review_data(self):
        url = reverse('reviews-detail', kwargs={'pk': self.review.id})
        response = self.client.get(url)
        expected_data = ReviewSerializer(self.review).data
        self.assertEqual(response.data, expected_data)


#Unit Test
class ReviewSerializerRatingTest(APITestCase):
    def test_valid_rating(self):
        serializer = ReviewSerializer()
        for valid_rating in range(1, 6):
            self.assertEqual(serializer.validate_rating(valid_rating), valid_rating)
            
    def test_validate_rating_below_range(self):
        serializer = ReviewSerializer()
        with self.assertRaises(ValidationError):
            serializer.validate_rating(0)

    def test_validate_rating_above_range(self):
        serializer = ReviewSerializer()
        with self.assertRaises(ValidationError):
            serializer.validate_rating(6)
