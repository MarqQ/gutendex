import json
import urllib
import requests
import urllib

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import BookReview
from .serializers import BookReviewSerializer


BASE_URL = 'https://gutendex.com/books/'


class ReviewListAPIView(APIView):
    """
    API VIEW - fetch all data from database
    """

    def get(self, request):
        reviews = BookReview.objects.all()
        serializer = BookReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookAPIView(APIView):
    """
    API VIEW - fetch data from gutendex
    """

    http_method_names = ['get', 'head']

    @staticmethod
    def get(self):

        r = requests.get(BASE_URL)
        if r.status_code == 200:
            raw_list = r.json()

            rating = 3.9
            # todo - all reviews need to be in a reviews_list = []
            reviews = [
                {'This is gooooooood',
                 'This is baaaaaaaad'
                 }
            ]

            book_list = []

            for books in raw_list['results']:
                book_list.append({
                    'id': books['id'],
                    'title': books['title'],
                    'authors': books['authors'],
                    'languages': books['languages'],
                    # 'authors': books['authors'][0]['name'],
                    # 'birth': books['authors'][0]['birth_year'],
                    # 'death': books['authors'][0]['death_year'],
                    # 'languages': books['languages'][0],
                    'download_count': books['download_count'],
                    'rating': rating,
                    'reviews': reviews
                })

            return Response(book_list)
