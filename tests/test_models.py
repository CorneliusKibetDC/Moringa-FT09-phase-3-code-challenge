

import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        # Pass the name correctly
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        # Create Author and Magazine objects to pass into Article
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title", "Test Content")
        
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")
        self.assertEqual(article.author.name, "John Doe")
        self.assertEqual(article.magazine.name, "Tech Weekly")

    def test_magazine_creation(self):
        # Pass the name and category correctly
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

if __name__ == "__main__":
    unittest.main()
