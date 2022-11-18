"""
books app URL Configuration
"""

from django.urls import path
from .views import BookAPIView
from .views import ReviewListAPIView, ReviewAPIView

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='books'),
    path('reviews/', ReviewListAPIView.as_view(), name='reviews'),
    path('reviews/<int:pk>/', ReviewAPIView.as_view(), name='change_review'),
]
