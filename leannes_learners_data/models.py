from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.safestring import mark_safe

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))
PUPILSTATUS = ((0, "No"), (1, "Yes"))

# code for Blog and COMMENT adapted
# from a previous walkthrough - Code Institues " I blog therefore I am"
class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField(
        folder='leannes_learners/blog_images/',
        transformation={'width': '400', 'height': '300', 'crop': 'fill',
                        'gravity': 'face', 'zoom': '0.5'},
        default='placeholder')
    alt_tag = models.CharField(max_length=200, blank=True)
    excerpt = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogPost_like', blank=True)

    def image_thumb(self):
        """
        This creates a thumbnail image of the current uploaded image
        """
        return mark_safe('<img src="{}" width="100" height="auto">'.format(
            self.featured_image.url))
    image_thumb.short_discription = "image"
    featured_image.allow_tags = True

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Blog Post Comment"
        verbose_name_plural = "Blog Post Comments"

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Carousel(models.Model):
    slide_identifying_name = models.CharField(max_length=80, unique=True)
    slide_text_headline = models.CharField(max_length=80, unique=False, blank=True)
    slide_text_description = models.CharField(max_length=200, blank=True)
    slide_image = CloudinaryField(
        folder='leannes_learners/caurosel_images/',
        transformation={'width': '1240', 'height': '700', 'crop': 'fill'},
        default='placeholder')

    alt_tag = models.CharField(max_length=200, blank=True)
    include_in_carousel = models.BooleanField(default=False)

    class Meta:
        ordering = ["-include_in_carousel", "-slide_identifying_name"]
        verbose_name = "Home Page Carousel content"
        verbose_name_plural = "Home Page Carousel content"

    def __str__(self):
        return self.slide_text_headline

    def image_thumb(self):
        """
        This creates a thumbnail image of the current uploaded image
        """
        return mark_safe('<img src="{}" width="100" height="auto">'.format(self.slide_image.url))
    image_thumb.short_discription = "image"
    slide_image.allow_tags = True


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


class Testimonial(models.Model):
    name = models.CharField(max_length=80, unique=True)
    testimonial_image = CloudinaryField(
        folder='leannes_learners/testimonial_images/',
        transformation={'width': '300', 'height': '400', 'crop': 'fill',
                        'gravity': 'face', 'zoom': '0.5'},
        default='placeholder')
    alt_tag = models.CharField(max_length=200, blank=True)
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


class Pass_plus(models.Model):
    name = models.CharField(max_length=80, unique=True)
    background_image = CloudinaryField(
        folder='leannes_learners/pass_plus/background_images/',
        transformation={'width': '300', 'height': '400', 'crop': 'fill',
                        'gravity': 'face', 'zoom': '0.5'},
        default='placeholder')
    background_image_alt_tag = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    focus_image = CloudinaryField(
        folder='leannes_learners/pass_plus/focus_images/',
        transformation={'width': '400', 'height': '400', 'crop': 'fill',
                        'gravity': 'face', 'zoom': '0.5'},
        default='placeholder')
    focus_image_alt_tag = models.CharField(max_length=200, blank=True)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def image_thumb(self):
        """
        This creates a thumbnail image of the current uploaded image
        """
        return mark_safe('<img src="{}" width="100" height="auto">'.format(
            self.focus_image.url))
    image_thumb.short_discription = "focus image"
    focus_image.allow_tags = True

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Pass Plus Page Content"
        verbose_name_plural = "Pass Plus Page Content"

    def __str__(self):
        return self.name