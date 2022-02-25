from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from blog.models import Category, Post, Comment
import json

from blog.views import PostLike


class TestBlogViews(TestCase):
	def setUp(self):
			self.client = Client()
			self.user = User.objects.create_user(
				username="admin", email="admin@myblog.com", password="password123!!")
			# self.login = self.client.login(username="admin", password="password123!!")
			
			self.category = Category.objects.create( name="my-great-first-blog-test_category")
			self.myfirstpost = Post.objects.create(
				title = "my-great-first-blog-post", 
				slug = "my-great-first-blog-post", 
				author = self.user, 
				featured_image = "my-great-first-blog.jpg", 
				alt_tag = "my_great_first_blog_image_description", 
				category  =self.category, 
				content = "This-is-my-great-first-blog-content", 
				excerpt = "This-is-my-great-first-blog-excerpt",
				)


			self.myfirstcomment = Comment.objects.create(
				comment = "My First Blog Post Comment",
				name = self.user,
				post= self.myfirstpost
				)
			
			self.blog_url = reverse('blog')
			# self.post_delete_url = reverse('post-delete')
			# self.post_update_url = reverse('post-update')
			self.category_url = reverse('category', args=['uncategorised'])
			self.post_detail_url = reverse('post-detail', args=['my-great-first-blog-post'])
			
			# self.comment_like_url = reverse('comment-like')
			# self.comment_dislike_url = reverse('comment-dislike')
			# self.comment_reply_url = reverse('comment-reply')
			# self.comment_delete_url = reverse('comment-delete')
			

	def test_category_list_GET(self):
		response = self.client.get(self.category_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/blog/category.html')

	def test_post_detail_create(self):
		post = get_object_or_404(Post, slug="my-great-first-blog-post")
		self.assertEqual(self.myfirstpost.title, "my-great-first-blog-post",)
		self.assertNotEqual(self.myfirstpost.title, "",)
		self.assertEqual(self.myfirstpost.content, "This-is-my-great-first-blog-content",)
		self.assertNotEqual(self.myfirstpost.content, "",)
		self.assertEqual(self.myfirstpost.featured_image, "my-great-first-blog.jpg",)
		self.assertEqual(self.myfirstpost.alt_tag, "my_great_first_blog_image_description",)
		self.assertNotEqual(self.myfirstpost.alt_tag, "",)
		self.assertEqual(self.myfirstpost.excerpt, "This-is-my-great-first-blog-excerpt",)
		self.assertNotEqual(self.myfirstpost.excerpt, "",)


	def test_post_detail_fetch(self):
		response = self.client.get(self.post_detail_url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/blog/post.html')

	# def test_add_comment(self):
	# 	post = get_object_or_404(Post, title="my-great-first-blog-post")
		
	# 	self.assertEqual(self.myfirstcomment.comment, "My First Blog Post Comment")
	# 	self.assertNotEqual(self.myfirstcomment.comment, "")

	# 	self.assertIsNotNone(self.myfirstcomment.post_id)
	# 	self.assertEqual(self.myfirstcomment.post_id, post.id)

	def test_blog_posts_fetch(self):
		response = self.client.get(self.blog_url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/blog/blog.html')


	def test_post_comment_create(self):
		self.assertEqual(self.myfirstcomment.comment, "My First Blog Post Comment",)
