"""
gutendex URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from books import main

urlpatterns = [
    path('', main.ReviewAPI.home),
    path('api/v1/', include('books.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
