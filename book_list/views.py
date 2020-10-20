from django.shortcuts import render
from book_list.filters import BookFilter
from book_list.models import Book
from django.views.generic import UpdateView,CreateView
from django.shortcuts import get_object_or_404

def book_list(request):
    book_list = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=book_list)
    return render(request, 'book/home.html', {'filter': book_filter})


class BookCreateView(CreateView):
    model = Book
    fields = "__all__"
    template_name = 'book/add.html'

class BookUpdateView(UpdateView):
    model = Book
    fields = "__all__"
    template_name = 'book/update.html'


