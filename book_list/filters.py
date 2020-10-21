import django_filters
from book_list.models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains", field_name="title")
    language = django_filters.CharFilter(lookup_expr="icontains", field_name="language")
    published_date__gt = django_filters.NumberFilter(
        field_name="published_date", lookup_expr="gt"
    )
    published_date__lt = django_filters.NumberFilter(
        field_name="published_date", lookup_expr="lt"
    )

    class Meta:
        model = Book
        fields = ("authors",)
