import json
import urllib
import requests
import urllib

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

BASE_URL = 'https://gutendex.com/books/'


class BookAPIView(APIView):
    """
    API VIEW 33ds
    """

    http_method_names = ['get', 'head']

    @staticmethod
    def get_book_list(self, request):
        req = requests.get(BASE_URL, timeout=60)
        a_dict = json.loads(req.text)
        # return a_dict
        return a_dict['results']