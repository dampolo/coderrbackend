from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from auth_app.models import Profile

class ReviewsTests(APITestCase):

    def setUp(self):
        # Create a user
        self.user = Profile.objects.create_user(
            username='testuser',
            password='pass123',
            email='test@example.com'
        )

        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_url(self):
        url = reverse('reviews-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)