from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from .views import create_checkout_session
from .views import check_pro_status
from .views import success_page, cancel_page
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('subscribe/', create_checkout_session, name='create-checkout-session'),
    path('ispro/', check_pro_status, name='check-pro-status'),
    path('success/', success_page, name='success'),
    path('cancel/', cancel_page, name='cancel'),
   
]
