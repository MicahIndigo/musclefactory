from django.urls import path
from . import views


urlpatterns = [
    path('buy/', views.create_checkout_session, name='buy_membership'),
    path('success/', views.checkout_success, name='checkout_success'),
]