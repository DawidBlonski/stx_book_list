import datetime

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models
from django.urls import reverse


def validate_year(value):
    if value < 1900 or value > datetime.datetime.now().year:
        raise ValidationError(f"{value} is not an correct year")


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=150, null=True)
    published_date = models.IntegerField(null=True, validators=[validate_year])
    isbn_number = models.CharField(max_length=13, null=True)
    page_count = models.IntegerField(null=True)
    thumbnail = models.URLField(max_length=255, null=True, validators=[URLValidator])
    language = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-list")
