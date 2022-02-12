from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.signals import request_finished
from django.dispatch import receiver
from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField


# Create your models here.

# Very Academy - Using Signals
@ receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)


class UserProfile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE,)
	user_bio =  models.CharField(max_length=2500, verbose_name = 'Biography', blank=False,)
	user_profile_image = CloudinaryField(
		folder='leannes_learners/user_profile_images/',
		transformation={'width': '300', 'height': '400', 'crop': 'fill',
						'gravity': 'face', 'zoom': '0.5'},
		default='image/upload/leannes_learners/default_image/bio_placeholder',
		unique_filename = True)
	user_facebook_url =  models.CharField(max_length=200, null=True, blank=True, verbose_name = 'Facebook Link')
	user_twitter_url =  models.CharField(max_length=200, null=True, blank=True, verbose_name = 'Twitter Link')
	user_linkedin_url =  models.CharField(max_length=200, null=True, blank=True, verbose_name = 'Linked-in Link')
	user_website_url =  models.CharField(max_length=200, null=True, blank=True, verbose_name = 'Website Link')

	def image_thumb(self):
		"""
		This creates a thumbnail image of the current uploaded image
		"""
		return mark_safe('<img src="{}" width="50" height="auto">'.format(
			self.user_profile_image.url))
	image_thumb.short_discription = "image"
	user_profile_image.allow_tags = True

	def __str__(self):
		return str(self.user)

