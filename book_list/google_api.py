import json
import requests
import urllib.parse
from book_list.models import Book
import datetime
import re

GOOGLE_API = "https://www.googleapis.com/books/v1/volumes"


def create_query(key_words, title, author):
    if not key_words:
        return
    key_words = urllib.parse.quote(key_words)
    if title:
        key_words += f"+intitle:{urllib.parse.quote(title)}"
    if author:
        key_words += f"+inauthor:{urllib.parse.quote(author)}"
    return key_words


def create_published_date(published_date):
    if published_date:
        year = re.search(r"\d{4}", published_date).group()
        return int(year)


def authors_to_string(authors):
    if authors:
        return next(iter(authors), None)


def get_isbn(isbns):
    return next(
        (isbn.get("identifier", "") for isbn in isbns if isbn.get("type") == "ISBN_13"),
        None,
    )


def get_books(key_words, title=None, author=None):
    parameters = create_query(key_words, title, author)
    response = requests.get(GOOGLE_API, {"q": parameters})
    if response.status_code != 200:
        return
    response_content = response.content.decode("utf-8")
    json_data = json.loads(response_content).get("items", None)
    if not json_data:
        return
    for element in json_data:
        volume_info = element.get("volumeInfo", {})
        title = volume_info.get("title")
        authors = authors_to_string(volume_info.get("authors"))
        published_date = create_published_date(volume_info.get("publishedDate", None))
        page_count = volume_info.get("pageCount", None)
        isbn_numbers = volume_info.get("industryIdentifiers", {})
        language = volume_info.get("language", None)
        isbn_number = get_isbn(isbn_numbers)
        print(isbn_number)
        thumbnail = volume_info.get("imageLinks", {}).get("thumbnail", None)
        yield {
            "title":title,
            "authors":authors,
            "published_date":published_date,
            "page_count":page_count,
            "language":language,
            "isbn_number":isbn_number,
            "thumbnail":thumbnail
        }

def books_to_database(key_words, title=None, author=None):
    Book.objects.bulk_create([Book(**i) for i in get_books(key_words, title, author)])
