from django.urls import path
from . import views
from django.urls import path
from . import views


urlpatterns = [
    path('process/', views.process_payment, name='process_payment'),
    path('api/process_payment/', views.process_payment_api, name='process_payment_api'),

]