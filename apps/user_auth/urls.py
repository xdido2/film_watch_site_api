from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.user_auth.views.forgot_password_view import ForgotPasswordActivateView, ForgotPasswordView
from apps.user_auth.views.register_view import RegisterView, ActivateAccountView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login_token'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),

    path('activate-register/<str:uidb64>/<str:token>',
         ActivateAccountView.as_view(), name='activate-account'),
    path('forgot-passoword/<str:uidb64>/<str:token>',
         ForgotPasswordActivateView.as_view(), name='forgot-password-activate'),

]
