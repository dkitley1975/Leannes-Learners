from dataclasses import field
from django.test import TestCase
from django.test import Client
from users.models import UserProfile


from ..forms import * 

class TestEditUserDetailsForm(TestCase):

	def test_EditUserDetails_valid_test_data_fills_all_required_fields(self):
		"""
		Test that the form is valid when all required fields are filled.
		"""
		form = EditUserDetailsForm(data={'first_name': 'Peter', 'last_name': 'Smith', 'username': 'P_Smith78', 'email': 'peter.smith@mymail.com'})
		self.assertTrue(form.is_valid())

	def test_EditUserDetails_invalid_test_data_missing_first_name(self):
		"""
		Test that the form is invalid when the first name is missing.
		"""
		form = EditUserDetailsForm(data={'first_name': '', 'last_name': 'Smith','username': 'P_Smith78', 'email': 'peter.smith@mymail.com'})
		self.assertFalse(form.is_valid())
		self.assertIn('first_name', form.errors.keys())
		self.assertEqual(form.errors['first_name'][0], 'This field is required.')

	def test_EditUserDetails_invalid_test_data_missing_last_name(self):
		"""
		Test that the form is invalid when the last name is missing.
		"""
		form = EditUserDetailsForm(data={'first_name': 'Peter', 'last_name': '','username': 'P_Smith78', 'email': 'peter.smith@mymail.com'})
		self.assertFalse(form.is_valid())
		self.assertIn('last_name', form.errors.keys())
		self.assertEqual(form.errors['last_name'][0], 'This field is required.')
	
	def test_EditUserDetails_invalid_test_data_missing_username(self):
		"""
		Test that the form is invalid when the username is missing.
		"""
		form = EditUserDetailsForm(data={'first_name': 'Peter', 'last_name': 'Smith', 'email': 'peter.smith@mymail.com'})
		self.assertFalse(form.is_valid())
		self.assertIn('username', form.errors.keys())
		self.assertEqual(form.errors['username'][0], 'This field is required.')

	def test_EditUserDetails_invalid_test_data_missing_email(self):
		"""
		Test that the form is invalid when the email is missing.
		"""
		form = EditUserDetailsForm(data={'first_name': 'Peter', 'last_name': 'Smith','username': 'P_Smith78', 'email': ''})
		self.assertFalse(form.is_valid())
		self.assertIn('email', form.errors.keys())
		self.assertEqual(form.errors['email'][0], 'This field is required.')

class TestRegistrationForm(TestCase):
	def test_RegistrationForm_valid_test_data_fills_all_required_fields(self):
		"""
		Test that the form is valid when all required fields are filled.
		"""
		form = RegistrationForm(data={'first_name': 'Peter', 'last_name': 'Smith', 'username': 'P_Smith78', 'email': 'peter.smith@mymail.com', 'password1': 'mypassword1', 'password2': 'mypassword1'})
		self.assertTrue(form.is_valid())

	def test_RegistrationForm_invalid_test_data_missing_first_name(self):
		"""
		Test that the form is invalid when the first name is missing.
		"""
		form = RegistrationForm(data={'first_name': '', 'last_name': 'Smith', 'username': 'P_Smith78', 'email': 'peter.smith@mymail.com', 'password1': 'mypassword1', 'password2': 'mypassword1'})
		self.assertFalse(form.is_valid())
		self.assertIn('first_name', form.errors.keys())
		self.assertEqual(form.errors['first_name'][0], 'This field is required.')
	
	def test_RegistrationForm_invalid_test_data_missing_last_name(self):
		"""
		Test that the form is invalid when the last name is missing.
		"""
		form = RegistrationForm(data={'first_name': 'Peter', 'last_name': '', 'username': 'P_Smith78', 'email': 'peter.smith@mymail.com', 'password1': 'mypassword1', 'password2': 'mypassword1'})
		self.assertFalse(form.is_valid())
		self.assertIn('last_name', form.errors.keys())
		self.assertEqual(form.errors['last_name'][0], 'This field is required.')
	
	def test_RegistrationForm_invalid_test_data_missing_username(self):
		"""
		Test that the form is invalid when the username is missing.
		"""
		form = RegistrationForm(data={'first_name': 'Peter', 'last_name': 'Smith', 'username': '', 'email': 'peter.smith@mymail.com', 'password1': 'mypassword1', 'password2': 'mypassword1'})
		self.assertFalse(form.is_valid())
		self.assertIn('username', form.errors.keys())
		self.assertEqual(form.errors['username'][0], 'This field is required.')
	
	def test_RegistrationForm_invalid_test_data_missing_email(self):
		"""
		Test that the form is invalid when the email is missing.
		"""
		form = RegistrationForm(data={'first_name': 'Peter', 'last_name': 'Smith', 'username': 'P_Smith78', 'email': '', 'password1': 'mypassword1', 'password2': 'mypassword1'})
		self.assertFalse(form.is_valid())
		self.assertIn('email', form.errors.keys())
		self.assertEqual(form.errors['email'][0], 'This field is required.')

	def test_RegistrationForm_invalid_test_data_missing_password1(self):
		"""
		Test that the form is invalid when the password1 is missing.
		"""
		form = RegistrationForm(data={'first_name': 'Peter', 'last_name': 'Smith', 'username': 'P_Smith78', 'email': 'peter.smith@mymail.com', 'password1': '', 'password2': 'mypassword1'})
		self.assertFalse(form.is_valid())
		self.assertIn('password1', form.errors.keys())
		self.assertEqual(form.errors['password1'][0], 'This field is required.')
	
	def test_RegistrationForm_invalid_test_data_missing_password2(self):
		"""
		Test that the form is invalid when the password2 is missing.
		"""
		form = RegistrationForm(data={'first_name': 'Peter', 'last_name': 'Smith', 'username': 'P_Smith78', 'email': 'peter.smith@mymail.com', 'password1': 'mypassword1', 'password2': ''})
		self.assertFalse(form.is_valid())
		self.assertIn('password2', form.errors.keys())
		self.assertEqual(form.errors['password2'][0], 'This field is required.')


class TestEditUserProfileForm(TestCase):

	def test_EditUserProfile_valid_test_data_fills_all_fields_filled(self):
		"""
		Test that the form is valid when all fields are filled.
		"""
		form = EditUserProfileForm(data={'user_bio': 'My user Bio', 'user_facebook_url': 'facebook_url', 'user_twitter_url': 'twitter_url', 'user_linkedin_url': 'linkedin_url', 'user_website_url': 'website_url'})
		self.assertTrue(form.is_valid())
	
	def test_EditUserProfile_valid_test_data_missing_bio_field(self):
		"""
		Test that the form is invalid when the user_bio field is missing.
		"""
		form = EditUserProfileForm(data={'user_bio': '', 'user_facebook_url': 'facebook_url', 'user_twitter_url': 'twitter_url', 'user_linkedin_url': 'linkedin_url', 'user_website_url': 'website_url'})
		self.assertFalse(form.is_valid())
		self.assertIn('user_bio', form.errors.keys())
		self.assertEqual(form.errors['user_bio'][0], 'This field is required.')

	def test_EditUserProfile_valid_test_data_only_user_bio_added(self):
		"""
		Test that the form is valid when the user_bio field is added.
		"""
		form = EditUserProfileForm(data={'user_bio': 'My user Bio'})
		self.assertTrue(form.is_valid())
		

	
	