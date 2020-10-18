from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name="authors")
    published_date = models.CharField(max_length=11, null=True)
    isbn_number = models.IntegerField(null=True)
    page_count = models.IntegerField(null=True)
    thumbnail = models.URLField(max_length=255, null=True)
    language = models.CharField(max_length=10,null=True)

