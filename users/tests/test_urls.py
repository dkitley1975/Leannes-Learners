from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from users.views import PasswordUpdateView, UserRegistrationView, EditUserDetailsForm, EditUserProfile
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


class TestUsersUrls(SimpleTestCase):
	""" Test the URLS """

	def test_password_update_url_resolves(self):
		"""
		Test that the url for amending user passwords is correct.
		"""
		url = reverse('change-password')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, PasswordUpdateView)

	def test_user_registration_url_resolves(self):
		"""
		Test that the url for user registration is correct.
		"""
		url = reverse('register')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, UserRegistrationView)
	
	def test_edit_user_details_url_resolves(self):
		"""
		Test that the url for editing the user details is correct.
		"""
		url = reverse('edit-user-details')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, EditUserDetailsForm)

	def test_edit_user_profile_url_resolves(self):
		"""
		Test that the url for editing the user profile is correct.
		"""
		url = reverse('edit-profile', args=['1'])
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, EditUserProfile)

	def test_password_reset_url_resolves(self):
		"""
		Test that the url for resetting the user password is correct.
		"""
		url = reverse('password_reset')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, PasswordResetView)

	def test_password_reset_done_url_resolves(self):
		"""
		Test that the url for user password done is correct.
		"""
		url = reverse('password_reset_done')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, PasswordResetDoneView)

	def test_password_reset_confirm_url_resolves(self):
		"""
		Test that the url for user password reset confirmation is correct.
		"""
		url = reverse('password_reset_confirm', args=['uidb64','token'])
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, PasswordResetConfirmView)

	def test_password_reset_completion_url_resolves(self):
		"""
		Test that the url for user password reset completion is correct.
		"""
		url = reverse('password_reset_complete')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, PasswordResetCompleteView)
