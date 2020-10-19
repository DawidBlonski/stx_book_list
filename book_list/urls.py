from django.urls import path

from book_list.views import book_list

urlpatterns = [
    path('', book_list, name='book-list'),
]