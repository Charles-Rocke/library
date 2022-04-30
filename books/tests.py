from django.test import TestCase
from django.urls import reverse
from .models import Book

# Create your tests here.
class BookTests(TestCase):
    # dummy info
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "A test title",
            subtitle = "A test subtitle",
            author = "Test Author",
            isbn = "1234567890123",
        )
    
    # test books content is consistent with dummy data
    def test_book_content(self):
        self.assertEqual(self.book.title, "A test title")
        self.assertEqual(self.book.subtitle, "A test subtitle")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.isbn, "1234567890123")
    
    # test view is consistent and gets the correct response codes  
    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A test subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")