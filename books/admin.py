from django.contrib import admin
from .models import BookReview


@admin.register(BookReview)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'rating', 'review')
