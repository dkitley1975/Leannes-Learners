from django.test import TestCase, Client
from blog.models import Category


class TestModels(TestCase):
    def setUp(self):
        """
        Set up the test category for the blog.
        """
        self.category = Category.objects.create(
            title="my-great-first-blog-test-category",
            slug="my-great-first-blog-test-category",
        )

    def test_category(self):
        """
        Test the category title.
        """
        self.assertEqual(
            self.category.title,
            "my-great-first-blog-test-category",
        )
