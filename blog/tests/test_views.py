from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Category, Post, Comment
import json


class TestBlogViews(TestCase):
	def setUp(self):
		self.client = Client()
		
		self.blog_url = reverse('blog')
		self.post_detail_url = reverse('post-detail', args=['post_details'])
		self.post_detils = Post.objects.create(
			title="my-great-first-blog",
			slug="my-great-first-blog",
			author="1",
			featured_image="my-great-first-blog.jpg",
			alt_tag="my_great_first_blog_image_description",
			category="my-great-first-blog-test_category",
			content="This-is-my-great-first-blog-content",
			excerpt="This-is-my-great-first-blog-excerpt",
			likes = "1"
		)














	def test_blogposts_GET(self):
		response = self.client.get(self.blog_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/blog/blog.html')


	def test_post_detail_GET(self):
		response = self.client.get(self.post_detail_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/blog/post.html')

	