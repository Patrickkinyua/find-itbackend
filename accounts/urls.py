from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from .views import (
    UserRegistrationView, UserLoginView, UserProfileView,
    UserProfileDetailView, ChangePasswordView, LogoutView,
    CustomTokenRefreshView
)

urlpatterns = [
    # Authentication endpoints
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Token management
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # User profile endpoints
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/settings/', UserProfileDetailView.as_view(), name='profile_settings'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]