from django.urls import path

from rest_book.views import BookView

urlpatterns = [
    path("/books", BookView.as_view(), name="rest-book"),
]
