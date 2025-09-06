"""
URL configuration for coderr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter 
from auth_app.api.views import ProfileViewSet, ProfilesCustomerViewSet, ProfilesBusinessViewSet
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'profiles/customer', ProfilesCustomerViewSet, basename='profiles-customer')
router.register(r'profiles/business', ProfilesBusinessViewSet, basename='profiles-business')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("auth_app.api.urls")),
    path("api/", include(router.urls)),  # This now includes all 3 ViewSets properly
    path("api/", include("offers_app.api.urls")),
    path("api/", include("orders_app.api.urls")),
    path("api/", include("reviews_app.api.urls")),
    path('api/', include("base_info_app.api.urls"))
] + staticfiles_urlpatterns()




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
