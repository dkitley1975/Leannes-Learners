from django.test import TestCase, Client
from django.urls import reverse
from users.views import PasswordUpdateView, UserRegistrationView, EditUserDetailsForm, EditUserProfile
import json

# class TestUsersViews(TestCase):
	# 	""" Test the URLS """
	# 	def setUp(self):
	# 	self.client = Client()
	# 	self.password_update_url = reverse('change-password')
	# 	self.user_registration_url = reverse('register')
	# 	self.edit_user_details_url = reverse('edit-user-details')
	# 	self.edit_user_profile_url = reverse('edit-profile', args=['1'])
	# 	self.password_reset_url = reverse('password-reset')
	# 	self.password_reset_done_url = reverse('password-reset-done')
	# 	self.password_reset_confirm_url = reverse('password-reset-confirm', args=['uidb64','token'])
	# 	self.password_reset_completion_url = reverse('password-reset-complete')
	

	# def test_password_update_url_resolves(self):
	# 	"""
	# 	Test that the url for amending user passwords is correct.
	# 	"""
	# 	response = self.client.get(self.password_update_url)
	# 	self.assertEquals(response.status_code, 302)
	# 	self.assertTemplateUsed(response, 'registration/change-password.html')

	# def test_user_registration_url_resolves(self):
	# 	"""
	# 	Test that the url for user registration is correct.
	# 	"""
	# 	response = self.client.get(self.user_registration_url)
	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'registration/register.html')
	
	# def test_edit_user_details_url_resolves(self):
	# 	"""
	# 	Test that the url for editing the user details is correct.
	# 	"""
	# 	response = self.client.get(self.edit_user_details_url)
	# 	self.assertEquals(response.status_code, 302)
	# 	self.assertTemplateUsed(response, 'registration/edit-user-details')

	# def test_edit_user_profile_url_resolves(self):
	# 	"""
	# 	Test that the url for editing the user profile is correct.
	# 	"""
	# 	response = self.client.get(self.edit_user_profile_url)
	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'registration/edit-profile.html')

	# def test_password_reset_url_resolves(self):
	# 	"""
	# 	Test that the url for resetting the user password is correct.
	# 	"""
	# 	response = self.client.get(self.password_reset_url)
	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'registration/password-reset-form.html')

	# def test_password_reset_done_url_resolves(self):
	# 	"""
	# 	Test that the url for user password done is correct.
	# 	"""
	# 	response = self.client.get(self.password_reset_done_url)
	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'registration/password-reset-done.html')

	# def test_password_reset_confirm_url_resolves(self):
	# 	"""
	# 	Test that the url for user password reset confirmation is correct.
	# 	"""
	# 	response = self.client.get(self.password_reset_confirm_url)
	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'registration/password-reset-confirm.html')

	# def test_password_reset_completion_url_resolves(self):
	# 	"""
	# 	Test that the url for user password reset completion is correct.
	# 	"""
	# 	response = self.client.get(self.password_reset_completion_url)
	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'registration/password-reset-complete.html')
