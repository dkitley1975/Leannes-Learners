from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.safestring import mark_safe

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


# code for Blog and COMMENT adapted
# from a previous walkthrough - Code Institues " I blog therefore I am"
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_posts"
    )
    featured_image = CloudinaryField(
        folder='leannes_learners/blog_images/',
        transformation={'width': '400', 'height': '300', 'crop': 'fill',
                        'gravity': 'face', 'zoom': '0.5'},
        default='placeholder')
    alt_tag = models.CharField(max_length=200, blank=True, verbose_name = 'Describe the image for the blind')
    excerpt = models.TextField(blank=True, verbose_name = 'Eye Catching Excerpt - make someone want to read the article')

    updated_at = models.DateTimeField(auto_now=True)
    content =  models.TextField()
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
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
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

