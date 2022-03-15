from django.test import TestCase, Client
from django.urls import reverse
from leannes_learners_data.models import About, Carousel, CompanyDetails, Instructors, Passplus, Service, TeachingHours, Terms, Testimonial
from blog.models import Post
import json


class TestLeannesLearnersDataViews(TestCase):
	""" Test the Views """

	def setUp(self):
		"""
		Set up the client and the urls for the views.
		"""
		self.client = Client()
		self.about_us_url = reverse('about-us')
		self.contact_us_url = reverse('contact-us')
		self.success_url = reverse('success')
		self.pass_plus_url = reverse('pass-plus')
		self.prices_url = reverse('prices')
		self.terms_and_conditions_url = reverse('terms-and-conditions')
		self.home_url = reverse('home')

	def test_about_us_GET(self):
		"""
		Test the about us page GET request.
		"""
		response = self.client.get(self.about_us_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/about-us.html')

	def test_contact_us_GET(self):
		"""
		Test the contact us page GET request.
		"""
		response = self.client.get(self.contact_us_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/contact-us.html')

	def test_contact_success_GET(self):
		"""
		Test the contact successful page GET request.
		"""
		response = self.client.get(self.success_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/success.html')

	def test_pass_plus_GET(self):
		"""
		Test the pass plus page GET request.
		"""
		response = self.client.get(self.pass_plus_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/pass-plus.html')

	def test_prices_information_page_GET(self):
		"""
		Test the prices and information page GET request.
		"""
		response = self.client.get(self.prices_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/prices.html')

	def test_terms_and_conditions_page_GET(self):
		"""
		Test the terms and conditions page GET request.
		"""
		response = self.client.get(self.terms_and_conditions_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/terms-and-conditions.html')

	def test_home_page_GET(self):
		"""
		Test the home page GET request.
		"""
		response = self.client.get(self.home_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')
