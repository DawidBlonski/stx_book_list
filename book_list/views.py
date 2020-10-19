from django.views.generic.list import ListView

from book_list.models import Book

class BookListView(ListView):
    model = Book
    paginate_by = 100
    template_name = 'book/home.html'