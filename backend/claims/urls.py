from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_claim, name='submit_claim'),
    path('success/', views.claim_success, name='claim_success'),
]