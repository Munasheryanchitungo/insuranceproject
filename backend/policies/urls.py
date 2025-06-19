from django.urls import path
from . import views

urlpatterns = [
    path('', views.policy_list, name='policy_list'),
    path('subscribe/', views.subscribe_policy, name='subscribe_policy'),
]