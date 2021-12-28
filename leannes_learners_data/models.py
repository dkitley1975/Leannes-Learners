from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


# code for POST and COMMENT adapted 
# from a previous walkthrough - Code Institues " I blog therefore I am"
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = models.ImageField(upload_to='leannes_learners_blog_images/', default='placeholder')
    alt_tag = models.CharField(max_length=200, blank=True)
    excerpt = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Services(models.Model):
    service_name = models.CharField(max_length=80, unique=True)
    service_description = models.CharField(max_length=200, blank=True)
    service_duration = models.CharField(max_length=80, blank=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-featured", "service_duration"]

    def __str__(self):
        return self.service_name


class HomeCarousel(models.Model):
    slide_identifying_name = models.CharField(max_length=80, unique=True)
    slide_text_headline = models.CharField(max_length=80, unique=False, blank=True)
    slide_text_description = models.CharField(max_length=200, blank=True)
    slide_image = models.ImageField(upload_to='leannes_learners_caurosel_images/', default='placeholder')

    alt_tag = models.CharField(max_length=200, blank=True)
    include_in_carousel = models.BooleanField(default=False)

    class Meta:
        ordering = ["-include_in_carousel", "-slide_identifying_name"]

    def __str__(self):
        return self.slide_text_headline
