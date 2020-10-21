from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import FormView

from book_list.filters import BookFilter
from book_list.forms import ApiForms
from book_list.google_api import books_to_database
from book_list.models import Book


def book_list(request):
    book_list = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=book_list)
    return render(request, "book/home.html", {"filter": book_filter})


class BookCreateView(CreateView):
    model = Book
    fields = "__all__"
    template_name = "book/add.html"


class BookUpdateView(UpdateView):
    model = Book
    fields = "__all__"
    template_name = "book/update.html"


class GoogleApiView(FormView):
    template_name = "book/api.html"
    form_class = ApiForms
    success_url = reverse_lazy("book-list")

    def form_valid(self, form):
        key_words = form.cleaned_data["key_words"]
        title = form.cleaned_data["title"]
        author = form.cleaned_data["author"]
        if not key_words:
            redirect("google-api")
        books_to_database(key_words, title, author)
        return redirect("book-list")
