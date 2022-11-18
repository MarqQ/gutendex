from django.test import TestCase
import requests


class GutendexAPI:
    url_parsed_from_gutendex = 'http://127.0.0.1:8000/api/v1/books/'

    def test_books(self):
        books = requests.get(url=self.url_parsed_from_gutendex)

        assert books.status_code == 200


class TestReviews:
    headers = {'Authorization': ''}
    url_reviews = 'http://127.0.0.1:8000/api/v1/reviews/'

    def test_get_reviews(self):
        reviews = requests.get(url=self.url_reviews, headers=self.headers)

        assert reviews.status_code == 200

    def test_get_review(self):
        reviews = requests.get(url=f'{self.url_reviews}1/', headers=self.headers)

        assert reviews.status_code == 200

    def test_post_review(self):
        new_review = {
            "book_id": 16389,
            "rating": "4",
            "review": "A good book to read"
        }
        sent_review = requests.post(url=self.url_reviews, headers=self.headers, data=new_review)

        assert sent_review.status_code == 201

    def test_put_review(self):
        put_review = {
            "book_id": 16389,
            "rating": 5,
            "review": "Very good book"
        }
        sent_review = requests.put(url=f'{self.url_reviews}1/', headers=self.headers, data=put_review)

        assert sent_review.status_code == 200

    def test_delete_review(self):
        delete_review = requests.put(url=f'{self.url_reviews}4/', headers=self.headers)

        assert delete_review.status_code == 204


