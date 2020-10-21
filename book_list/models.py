from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
import datetime

def validate_isbn(value):
    if not any(i.isdigit() for i in value) or len(value) != 13:
        raise ValidationError(f"{value} is not a isbn number")

def validate_year(value):
    if value < 1900 or value > datetime.datetime.now().year:
        raise ValidationError(f"{value} is not an correct year")

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=150, null=True)
    published_date = models.IntegerField(null=True,validators=[validate_year])
    isbn_number = models.CharField(max_length=13,null=True,validators=[validate_isbn])
    page_count = models.IntegerField(null=True)
    thumbnail = models.URLField(max_length=255, null=True,validators=[URLValidator])
    language = models.CharField(max_length=10, null=True)

    def get_absolute_url(self):
        return reverse("book-list")
