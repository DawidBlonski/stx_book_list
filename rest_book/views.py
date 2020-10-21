from rest_framework.filters import OrderingFilter
from rest_framework import generics
from book_list.models import Book
from django_filters.rest_framework import DjangoFilterBackend
from rest_book.serializers import BookSerializer
from book_list.filters import BookFilter
class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = BookFilter
    ordering_fields = ["published_date"]

