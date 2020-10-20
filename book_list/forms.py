from django.forms import modelformset_factory
from book_list.models import Book

BookFormSet = modelformset_factory(Book, fields = '__all__' )