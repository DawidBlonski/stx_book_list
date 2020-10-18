from django.test import TestCase
from .models import Author,Book

class AuthorTest(TestCase):

    def create_author(self,name='Autor'):
            return Author.objects.create(name=name)

    def test_author(self):
        author = self.create_author()
        self.assertTrue(isinstance(author,Author))
        self.assertEqual(author.__str__(),author.name)
        self.assertEqual('Autor',author.name)

class BookTest(TestCase):

    def create_book(self,name='Autor'):
            return Author.objects.create(name=name)

    def test_author(self):
        author = self.create_author()
        self.assertTrue(isinstance(author,Author))
        self.assertEqual(author.__str__(),author.name)
        self.assertEqual('Autor',author.name)
