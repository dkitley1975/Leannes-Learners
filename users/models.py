from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField


# Create your models here.

# Very Academy - Using Signals
@ receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    When a user is created, create a profile for them.
    @param sender - the sender of the signal (User)
    @param instance - the instance of the user (User)
    @param created - whether the user was created (boolean)
    @param kwargs - the keyword arguments (dict)
    """
    if created:
        UserProfile.objects.create(user=instance)


class UserProfile(models.Model):
    """
    Create a user profile for the user.
    @param user - the user's profile
    @returns the user's profile
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE,)
    user_bio =  models.CharField(max_length=2500, blank=False,
        verbose_name = 'Biography')
    user_profile_image = CloudinaryField(
        folder='leannes_learners/user_profile_images/',
        transformation={
            'width': '300',
            'height': '400',
            'crop': 'fill',
            'gravity': 'face',
            'zoom': '0.5'
            },
        default='image/upload/leannes_learners/default_image/bio_placeholder',
        unique_filename = True)
    user_facebook_url =  models.CharField(max_length=200, null=True, blank=True,
        verbose_name = 'Facebook Link')
    user_twitter_url =  models.CharField(max_length=200, null=True, blank=True,
        verbose_name = 'Twitter Link')
    user_linkedin_url =  models.CharField(max_length=200, null=True, blank=True,
        verbose_name = 'Linked-in Link')
    user_website_url =  models.CharField(max_length=200, null=True, blank=True,
        verbose_name = 'Website Link')

    def image_thumb(self):
        """ Create a thumbnail for the user's profile image.
        @returns the thumbnail """
        return mark_safe('<img src="{}" width="50" height="auto">'.format(
            self.user_profile_image.url))
        image_thumb.short_discription = "image"
        user_profile_image.allow_tags = True

    def __str__(self):
        return str(self.user)
