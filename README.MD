# GUTENDEX API

This is an API to search books from a third-party API and record reviews and ratings for each book.

This project was developed with:

- Python 3.9.6
- Django 3.2.16
- Django Rest Framework 3.14
- SQLite3

###To run this project

- python -m venv .venv
- pip install django==3.2.16
- pip install requirements.txt
- pyhon manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser (if necessary to see the admin panel)
- python manage.py runserver

##Basics about the project

This project is based on [gutendex](https://gutendex.com/), an public API with a collection of book details.
The objective of this project is to provide an API based on the Gutendex API, providing the option to register reviews 
and ratings on books, and provide this data along with the data for each book.

##BOOK APP

The app **books** contem os models, views, serializers e rotas para os endpoints.

###views.py
In the view.py module are the methods for acquiring data from the gutendex API (class BookAPIView(APIView) and for the 
CRUD of reviews (**ReviewListAPIView(generics.ListCreateAPIView** and **ReviewAPIView(generics.RetrieveUpdateDestroyAPIView**)

I chose to work with generic methods because they are less verbose and have the Restful methods 'behind the curtains' and 
cover 80% of the use cases for restful verbs.

###models.py

In the models module, it handles the interaction with the database for the Reviews method.

###serializers.py
This is data serialization as well as rating validation.

###books\urls.py

Here are the API urls:
- [Fetch all books from gutendex](http://127.0.0.1:8000/api/v1/books/)
- [Fetch all data from database - reviews](http://127.0.0.1:8000/api/v1/reviews/)
- [Fetch a unique data from database - review](http://127.0.0.1:8000/api/v1/reviews/1/)


###gutendex\urls.py

Contains the generic urls, login, admin, etc.

