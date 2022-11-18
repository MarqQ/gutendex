from rest_framework import serializers
from django.db.models import Avg
from .models import BookReview


class BookReviewSerializer(serializers.ModelSerializer):

    # average_rating = serializers.SerializerMethodField()

    class Meta:
        # extra_kwargs = {
        #     'book_id': {'write_only': True}
        # }
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

    # def get_average_rating(self, obj):
    #     average = obj.rating.aggregate(Avg('rating')).get('rating__avg')
    #
    #     if average is None:
    #         return 0
    #     return round(average * 2) / 2
