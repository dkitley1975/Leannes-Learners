from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.safestring import mark_safe

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class About(models.Model):
    short_description = models.CharField(max_length=80, unique=True)
    about_us = models.TextField()
    background_image = CloudinaryField(
        folder='leannes_learners/about_us/background_images/',
        default='placeholder')
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def image_thumb(self):
        """
        This creates a thumbnail image of the current uploaded image
        """
        return mark_safe('<img src="{}" width="auto" height="100">'.format(
            self.background_image.url))
    image_thumb.short_discription = "background image"
    background_image.allow_tags = True 

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.short_description


class Carousel(models.Model):
    slide_identifying_name = models.CharField(max_length=80, unique=True)
    slide_text_headline = models.CharField(max_length=80, unique=False, blank=True)
    slide_text_description = models.TextField(max_length=200, blank=True)
    slide_image = CloudinaryField(
        folder='leannes_learners/caurosel_images/',
        transformation={'width': '1240', 'height': '700', 'crop': 'fill'},
        default='placeholder')

    alt_tag = models.CharField(max_length=200, blank=True, verbose_name = 'Describe the image for the blind')
    include_in_carousel = models.BooleanField(default=False)

    class Meta:
        ordering = ["-include_in_carousel", "-slide_identifying_name"]
        verbose_name = "Carousel on Home Page"
        verbose_name_plural = "Carousel on Home Page"

    def __str__(self):
        return self.slide_text_headline

    def image_thumb(self):
        """
        This creates a thumbnail image of the current uploaded image
        """
        return mark_safe('<img src="{}" width="100" height="auto">'.format(self.slide_image.url))
    image_thumb.short_discription = "image"
    slide_image.allow_tags = True


class Instructors(models.Model):
    name = models.CharField(max_length=80, unique=True)
    instructor_image = CloudinaryField(
        folder='leannes_learners/instructor_images/',
        transformation={'width': '300', 'height': '400', 'crop': 'fill',
                        'gravity': 'face', 'zoom': '0.5'},
        default='placeholder')
    alt_tag = models.CharField(max_length=200, blank=True, verbose_name = 'Describe the image for the blind')
    about = models.TextField()
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def image_thumb(self):
        """
        This creates a thumbnail image of the current uploaded image
        """
        return mark_safe('<img src="{}" width="100" height="auto">'.format(
            self.instructor_image.url))
    image_thumb.short_discription = "image"
    instructor_image.allow_tags = True

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Driving Instructor"
        verbose_name_plural = "Driving Instructors"

    def __str__(self):
        return self.name


class Service(models.Model):
    service_name = models.CharField(max_length=80, unique=True)
    service_description = models.CharField(max_length=200, blank=True)
    service_duration = models.CharField(max_length=80, blank=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-featured", "service_duration"]
        verbose_name = "Service Description"
        verbose_name_plural = "Service Descriptions"

    def __str__(self):
        return self.service_name


class Passplus(models.Model):
    short_description = models.CharField(max_length=80, unique=True)
    background_image = CloudinaryField(
        folder='leannes_learners/pass_plus/background_images/',
        default='placeholder')
    lead_content = models.TextField()
    main_content = models.TextField()
    focus_image = CloudinaryField(
        folder='leannes_learners/pass_plus/focus_images/',
        transformation={'width': '400', 'height': '400', 'crop': 'fill',
                        'gravity': 'face', 'zoom': '0.5'},
        default='placeholder')
    alt_tag = models.CharField(max_length=200, blank=True, verbose_name = 'Describe the image for the blind')
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def image_thumb(self):
        """
        This creates a thumbnail image of the current uploaded image
        """
        return mark_safe('<img src="{}" width="auto" height="100">'.format(
            self.background_image.url))
    image_thumb.short_discription = "background image"
    background_image.allow_tags = True

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Pass Plus Page"
        verbose_name_plural = "Pass Plus Page"

    def __str__(self):
        return self.short_description


class Terms(models.Model):
    background_image = CloudinaryField(
        folder='leannes_learners/terms_and_conditions/background_images/',
        default='placeholder')
    lead_content = models.TextField()
    main_content = models.TextField()
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def image_thumb(self):
        """
        This creates a thumbnail image of the current uploaded image
        """
        return mark_safe('<img src="{}" width="auto" height="100">'.format(
            self.background_image.url))
    image_thumb.short_discription = "terms_and_conditions"
    background_image.allow_tags = True

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Terms and Conditions Page"
        verbose_name_plural = "Terms and Conditions Page"
   
    def __str__(self):
        return "Terms and Conditions"


class Testimonial(models.Model):
    name = models.CharField(max_length=80, unique=True)
    testimonial_image = CloudinaryField(
        folder='leannes_learners/testimonial_images/',
        transformation={'width': '300', 'height': '400', 'crop': 'fill',
                        'gravity': 'face', 'zoom': '0.5'},
        default='placeholder')
    alt_tag = models.CharField(max_length=200, blank=True, verbose_name = 'Describe the image for the blind')
    testimonial = models.TextField()
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def image_thumb(self):
        """
        This creates a thumbnail image of the current uploaded image
        """
        return mark_safe('<img src="{}" width="100" height="auto">'.format(
            self.testimonial_image.url))
    image_thumb.short_discription = "image"
    testimonial_image.allow_tags = True

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.name


class CompanyDetails(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    social_media_name = models.CharField(max_length=80, blank=True)
    social_media_link = models.CharField(max_length=200, blank=True)
    social_media_image = CloudinaryField(
        folder='leannes_learners/contact_page/social_images/',
        transformation={'width': 'auto', 'height': '50', 'crop': 'fill'},
        default='placeholder')
    social_media_name_2 = models.CharField(max_length=80, blank=True)
    social_media_link_2 = models.CharField(max_length=200, blank=True)
    social_media_image_2 = CloudinaryField(
        folder='leannes_learners/contact_page/social_images/',
        transformation={'width': 'auto', 'height': '50', 'crop': 'fill'},
        default='placeholder')
    social_media_name_3 = models.CharField(max_length=80, blank=True)
    social_media_link_3 = models.CharField(max_length=200, blank=True)
    social_media_image_3 = CloudinaryField(
        folder='leannes_learners/contact_page/social_images/',
        transformation={'width': 'auto', 'height': '50', 'crop': 'fill'},
        default='placeholder')
    social_media_name_4 = models.CharField(max_length=80, blank=True)
    social_media_link_4 = models.CharField(max_length=200, blank=True)
    social_media_image_4 = CloudinaryField(
        folder='leannes_learners/contact_page/social_images/',
        transformation={'width': 'auto', 'height': '50', 'crop': 'fill'},
        default='placeholder')

    class Meta:
        # ordering = ["-id"]
        verbose_name = "Company Contact/Social Information"
        verbose_name_plural = "Company Contact/Social Information"

    def __str__(self):
        return self.phone


class TeachingHours(models.Model):
    day = models.CharField(max_length=9, unique=True)
    start_time = models.CharField(max_length=6)
    finish_time = models.CharField(max_length=6, blank=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Teaching Hours"
        verbose_name_plural = "Teaching Hours"
