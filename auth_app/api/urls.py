from django.urls import path
from .views import RegistrationView, CustomLoginView, ProfilesCustomerViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("api/registration/", RegistrationView.as_view(), name="registration"),
    path("api/login/", CustomLoginView.as_view(), name="login"),
]