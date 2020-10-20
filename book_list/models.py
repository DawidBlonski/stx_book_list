from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=150, null=True)
    published_date = models.IntegerField(null=True)
    isbn_number = models.CharField(max_length=13,null=True)
    page_count = models.IntegerField(null=True)
    thumbnail = models.URLField(max_length=255, null=True)
    language = models.CharField(max_length=10, null=True)

    def get_absolute_url(self):
        return reverse("book-list")
