from django.shortcuts import render
import requests

BASE_URL = 'https://gutendex.com/books'


class ReviewAPI:

    def home(request):
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

            for books in raw_list['results']:
                book_list.append({
                    'id': books['id'],
                    'title': books['title'],
                    'authors': books['authors'],
                    'languages': books['languages'],
                    'download_count': books['download_count'],
                    'reviews': review_list
                })

            raw_review = []

            for i in raw_list['results']:
                for x in reviews_json:
                    if i['id'] == x['book_id']:
                        raw_review.append({
                            'id': i['id'],
                            'title': i['title'],
                            'authors': i['authors'],
                            'languages': i['languages'],
                            'download_count': i['download_count'],
                            'reviews': reviews_json
                        })

            review_parser = []

            livro = [{'id': 2641, 'title': 'A Room with a View', 'authors': [{'name': 'Forster, E. M. (Edward Morgan)', 'birth_year': 1879, 'death_year': 1970}], 'languages': ['en'], 'download_count': 176667, 'reviews': [{'book_id': 2641, 'rating': '4', 'review': 'A good book to read'}, {'book_id': 145, 'rating': '5', 'review': 'I like this book'}, {'book_id': 67979, 'rating': '5', 'review': 'Surprised to read this'}, {'book_id': 394, 'rating': '5', 'review': 'Very good book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}]}, {'id': 145, 'title': 'Middlemarch', 'authors': [{'name': 'Eliot, George', 'birth_year': 1819, 'death_year': 1880}], 'languages': ['en'], 'download_count': 163592, 'reviews': [{'book_id': 2641, 'rating': '4', 'review': 'A good book to read'}, {'book_id': 145, 'rating': '5', 'review': 'I like this book'}, {'book_id': 67979, 'rating': '5', 'review': 'Surprised to read this'}, {'book_id': 394, 'rating': '5', 'review': 'Very good book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}]}, {'id': 67979, 'title': 'The Blue Castle: a novel', 'authors': [{'name': 'Montgomery, L. M. (Lucy Maud)', 'birth_year': 1874, 'death_year': 1942}], 'languages': ['en'], 'download_count': 141840, 'reviews': [{'book_id': 2641, 'rating': '4', 'review': 'A good book to read'}, {'book_id': 145, 'rating': '5', 'review': 'I like this book'}, {'book_id': 67979, 'rating': '5', 'review': 'Surprised to read this'}, {'book_id': 394, 'rating': '5', 'review': 'Very good book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}]}, {'id': 394, 'title': 'Cranford', 'authors': [{'name': 'Gaskell, Elizabeth Cleghorn', 'birth_year': 1810, 'death_year': 1865}], 'languages': ['en'], 'download_count': 138706, 'reviews': [{'book_id': 2641, 'rating': '4', 'review': 'A good book to read'}, {'book_id': 145, 'rating': '5', 'review': 'I like this book'}, {'book_id': 67979, 'rating': '5', 'review': 'Surprised to read this'}, {'book_id': 394, 'rating': '5', 'review': 'Very good book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}]}, {'id': 16389, 'title': 'The Enchanted April', 'authors': [{'name': 'Von Arnim, Elizabeth', 'birth_year': 1866, 'death_year': 1941}], 'languages': ['en'], 'download_count': 130572, 'reviews': [{'book_id': 2641, 'rating': '4', 'review': 'A good book to read'}, {'book_id': 145, 'rating': '5', 'review': 'I like this book'}, {'book_id': 67979, 'rating': '5', 'review': 'Surprised to read this'}, {'book_id': 394, 'rating': '5', 'review': 'Very good book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}]}, {'id': 16389, 'title': 'The Enchanted April', 'authors': [{'name': 'Von Arnim, Elizabeth', 'birth_year': 1866, 'death_year': 1941}], 'languages': ['en'], 'download_count': 130572, 'reviews': [{'book_id': 2641, 'rating': '4', 'review': 'A good book to read'}, {'book_id': 145, 'rating': '5', 'review': 'I like this book'}, {'book_id': 67979, 'rating': '5', 'review': 'Surprised to read this'}, {'book_id': 394, 'rating': '5', 'review': 'Very good book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}]}, {'id': 16389, 'title': 'The Enchanted April', 'authors': [{'name': 'Von Arnim, Elizabeth', 'birth_year': 1866, 'death_year': 1941}], 'languages': ['en'], 'download_count': 130572, 'reviews': [{'book_id': 2641, 'rating': '4', 'review': 'A good book to read'}, {'book_id': 145, 'rating': '5', 'review': 'I like this book'}, {'book_id': 67979, 'rating': '5', 'review': 'Surprised to read this'}, {'book_id': 394, 'rating': '5', 'review': 'Very good book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}]}]
            revisao = [{'book_id': 2641, 'rating': '4', 'review': 'A good book to read'}, {'book_id': 145, 'rating': '5', 'review': 'I like this book'}, {'book_id': 67979, 'rating': '5', 'review': 'Surprised to read this'}, {'book_id': 394, 'rating': '5', 'review': 'Very good book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}, {'book_id': 16389, 'rating': '2', 'review': 'Not so cool book'}]

            for h in revisao:
                for j in livro:
                    if j['id'] == h['book_id']:
                        review_parser.append({
                            'id': j['id'],
                            'title': j['title'],
                            'authors': j['authors'],
                            'languages': j['languages'],
                            'download_count': j['download_count'],
                            'REVIEW_BOOK_ID': h['book_id'],
                            'RATING': h['rating'],
                            'REVIEW': h['review']
                        })

            return render(request, 'home.html', {
                'x': review_list,
                'z': raw_review,
                'f': review_parser,
                'y': book_list
            })
