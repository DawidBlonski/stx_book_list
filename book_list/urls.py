from django.urls import path

from book_list.views import book_list, BookCreateView, BookUpdateView, GoogleApiView

urlpatterns = [
    path("", book_list, name="book-list"),
    path("google_api/", GoogleApiView.as_view(), name="google-api"),
    path("add/", BookCreateView.as_view(), name="book-create"),
    path("update/<int:pk>", BookUpdateView.as_view(), name="book-update"),
]
