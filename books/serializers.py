from rest_framework import serializers
from .models import BookReview


class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = (
            'book_id',
            'rating',
            'review'
        )

    def validate_rating(self, rating):
        if rating in range(0, 6):
            return rating
        raise serializers.ValidationError('Rating needs to be between 0 and 5')
