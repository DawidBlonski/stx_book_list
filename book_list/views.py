from django.shortcuts import render
from book_list.filters import BookFilter
from book_list.models import Book

def book_list(request):
    book_list = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=book_list)
    return render(request, 'book/home.html', {'filter': book_filter})