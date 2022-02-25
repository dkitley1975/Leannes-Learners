from dataclasses import field
from django.test import TestCase
from django.test import Client

from ..forms import *

class TestContactForm(TestCase):

	def test_ContactForm_valid_test_data_fills_all_fields(self):
			''' 
			Test all the fields are filled - 
			fills with test data
			'''
			form = ContactForm(data={'first_name': 'Peter', 'last_name': 'Smith', 'email': 'peter.smith@mymail.com', 'phone': '07123456789', 'postcode': 'hd8 7hd', 'message': "I would like to drive please ring me"})
			self.assertTrue(form.is_valid())

	def test_ContactForm_invalid_test_data_missing_first_name(self):
			''' 
			Test all the fields are filled - 
			fills with test data - 
			but misses the first name
			'''
			form = ContactForm(data={'first_name': '', 'last_name': 'Smith', 'email': 'peter.smith@mymail.com', 'phone': '07123456789', 'postcode': 'hd8 7hd', 'message': "I would like to drive please ring me"})
			self.assertFalse(form.is_valid())
			self.assertIn('first_name', form.errors.keys())
			self.assertEqual(form.errors['first_name'][0], 'This field is required.')

	def test_ContactForm_invalid_test_data_missing_last_name(self):
			''' 
			Test all the fields are filled - 
			fills with test data - 
			but misses the last name
			'''
			form = ContactForm(data={'first_name': 'Peter', 'last_name': '', 'email': 'peter.smith@mymail.com', 'phone': '07123456789', 'postcode': 'hd8 7hd', 'message': "I would like to drive please ring me"})
			self.assertFalse(form.is_valid())
			self.assertIn('last_name', form.errors.keys())
			self.assertEqual(form.errors['last_name'][0], 'This field is required.')

	def test_ContactForm_invalid_test_data_missing_email(self):
			''' 
			Test all the fields are filled - 
			fills with test data - 
			but misses the email
			'''
			form = ContactForm(data={'first_name': 'Peter', 'last_name': 'Smith', 'email': '', 'phone': '07123456789', 'postcode': 'hd8 7hd', 'message': "I would like to drive please ring me"})
			self.assertFalse(form.is_valid())
			self.assertIn('email', form.errors.keys())
			self.assertEqual(form.errors['email'][0], 'This field is required.')

	def test_ContactForm_invalid_test_data_missing_phone(self):
			''' 
			Test all the fields are filled - 
			fills with test data - 
			but misses the phone
			'''
			form = ContactForm(data={'first_name': 'Peter', 'last_name': 'Smith', 'email': 'peter.smith@mymail.com', 'phone': '', 'postcode': 'hd8 7hd', 'message': "I would like to drive please ring me"})
			self.assertFalse(form.is_valid())
			self.assertIn('phone', form.errors.keys())
			self.assertEqual(form.errors['phone'][0], 'This field is required.')
	
	def test_ContactForm_invalid_test_data_missing_postcode(self):
			''' 
			Test all the fields are filled - 
			fills with test data - 
			but misses the postcode
			'''
			form = ContactForm(data={'first_name': 'Peter', 'last_name': 'Smith', 'email': 'peter.smith@mymail.com', 'phone': '07123456789', 'postcode': '', 'message': "I would like to drive please ring me"})
			self.assertFalse(form.is_valid())
			self.assertIn('postcode', form.errors.keys())
			self.assertEqual(form.errors['postcode'][0], 'This field is required.')
	
	def test_ContactForm_valid_test_data_missing_message(self):
			''' 
			Test all the fields are filled - 
			fills with test data - 
			but misses the message
			'''
			form = ContactForm(data={'first_name': 'Peter', 'last_name': 'Smith', 'email': 'peter.smith@mymail.com', 'phone': '07123456789', 'postcode': 'hd8 7hd', 'message': ""})
			self.assertFalse(form.is_valid())
			self.assertIn('message', form.errors.keys())
			self.assertEqual(form.errors['message'][0], 'This field is required.')
	
	def test_ContactForm_valid_test_data_missing_name_message(self):
			''' 
			Test all the fields are filled - 
			fills with test data - 
			but misses the first name and the message
			'''
			form = ContactForm(data={'first_name': '', 'last_name': 'Smith', 'email': 'peter.smith@mymail.com', 'phone': '07123456789', 'postcode': 'hd8 7hd', 'message': ""})
			self.assertFalse(form.is_valid())

