from django.urls import path

from book_list.views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
]