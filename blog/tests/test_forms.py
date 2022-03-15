from dataclasses import field
from django.test import TestCase
from django.test import Client

from ..forms import *


class TestCommentForm(TestCase):

	def test_comment_body_is_required(self):
		"""
		this is a test comment body is required 
		"""
		form = CommentForm({'comment': ''})
		self.assertFalse(form.is_valid())
		self.assertIn('comment', form.errors.keys())
		self.assertEqual(form.errors['comment'][0], 'This field is required.')

	def test_body_field_is_not_required(self):
		"""
		Test that the form is valid when the body field is not required.
		"""
		form = CommentForm({'comment': 'Test Comment'})
		self.assertTrue(form.is_valid())

	def test_fields_are_explicit_in_form_metaclass(self):
		"""
		Check that the form has the correct fields.
		"""
		form = CommentForm()
		self.assertEqual(form.Meta.fields, ('comment',))
