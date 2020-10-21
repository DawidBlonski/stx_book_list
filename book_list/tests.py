from django.test import TestCase
from django.urls import reverse

from book_list.models import Book

THUMBNAIL = """ttp://books.google.com/books/content?id=m4_UDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"""


class BookModelTest(TestCase):
    def setUp(self) -> None:
        self.correct_book, _ = Book.objects.get_or_create(
            title="Test",
            authors="Autor",
            published_date=2017,
            isbn_number=9781789620528,
            page_count=5,
            thumbnail=THUMBNAIL,
            language="PL",
        )

    def test_fields(self):
        self.assertEqual(self.correct_book.title, "Test")
        self.assertEqual(self.correct_book.authors, "Autor")
        self.assertEqual(self.correct_book.published_date, 2017)
        self.assertEqual(self.correct_book.isbn_number, 9781789620528)
        self.assertEqual(self.correct_book.page_count, 5)
        self.assertEqual(self.correct_book.thumbnail, THUMBNAIL)
        self.assertEqual(self.correct_book.language, "PL")


class BookViewTest(TestCase):
    def setUp(self) -> None:
        self.correct_book, _ = Book.objects.get_or_create(
            title="Test",
            authors="Autor",
            published_date=2017,
            isbn_number=9781789620528,
            page_count=5,
            thumbnail=THUMBNAIL,
            language="PL",
        )

    def test_get_list(self):
        response = self.client.get("")
        reverse_url = reverse("book-list")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.get(reverse_url).status_code, 200)

    def test_add_view(self):
        response = self.client.get(reverse("book-create"))
        self.assertEqual(response.status_code, 200)

    def test_update_view(self):
        book = Book.objects.get(title=self.correct_book).pk
        response = self.client.get(reverse("book-update", kwargs={"pk": book}))
        self.assertEqual(response.status_code, 200)

    def test_google_api_view(self):
        response = self.client.get(reverse("google-api"))
        self.assertEqual(response.status_code, 200)
