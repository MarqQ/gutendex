import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import BookReview
from .serializers import BookReviewSerializer


BASE_URL = 'https://gutendex.com/books/'


class ReviewListAPIView(generics.ListCreateAPIView):
    """
    API VIEW - fetch all data from database
    """

    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer


class ReviewAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API VIEW - fetch unique data from database
    """

    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer


class BookAPIView(APIView):
    """
    API VIEW - fetch all books from gutendex
    """

    http_method_names = ['get', 'head']

    @staticmethod
    def get(self):

        r = requests.get(BASE_URL)
        if r.status_code == 200:
            raw_list = r.json()

            reviews = requests.get('http://127.0.0.1:8000/api/v1/reviews/')
            reviews_json = reviews.json()

            review_list = []
            for review in reviews_json:
                review_list.append({
                    'book_id': review['book_id'],
                    'rating': review['rating'],
                    'review': review['review'],
                })

            book_list = []

            for book_review in reviews_json:
                for book_rated in raw_list['results']:
                    if book_rated['id'] == book_review['book_id']:
                        book_list.append({
                            'id': book_rated['id'],
                            'title': book_rated['title'],
                            'authors': book_rated['authors'],
                            'languages': book_rated['languages'],
                            'download_count': book_rated['download_count'],
                            'rating': book_review['rating'],
                            'review': book_review['review']
                        })

            return Response(book_list)
