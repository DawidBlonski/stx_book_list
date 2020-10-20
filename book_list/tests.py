from django.test import TestCase


class AuthorTest(TestCase):
    def setUp(self) -> None:
        self.author = self.create_author()

    def create_author(self, name="Autor"):
        return Author.objects.create(name=name)

    def author_is_instance(self):
        self.assertTrue(isinstance(self.author, Author))

    def test__str__(self):
        self.assertEqual(self.author.__str__(), self.author.name)

    def test_author_value(self):
        self.assertEqual("Autor", self.author.name)
