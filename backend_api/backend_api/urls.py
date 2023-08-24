"""
URL configuration for backend_api project.

"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('main.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Get Token with username and password
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refresh token if expired
    path('api-auth/',include('rest_framework.urls')), 

]
