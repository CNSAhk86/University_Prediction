from django.urls import path
from .views import predict  # Correct import

urlpatterns = [
    path('', predict, name='predict'),
]
