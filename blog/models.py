from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.safestring import mark_safe
from users.models import UserProfile
from autoslug import AutoSlugField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """
    A model for the categories of the dataset.
    """

    title = models.CharField(max_length=50)
    slug = AutoSlugField(max_length=60, populate_from="title", unique=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        """
        returns the title of the category
        """
        return self.title

    def __str__(self):
        """
        Return the name of the object.
        """
        return self.slug


class Post(models.Model):
    """
    The Post model for the blog. This is the model that will be used to store the blog posts.
    @param title - the title of the post
    @param slug - the slug of the post
    @param author - the author of the post
    @param featured_image - the featured image of the post
    @param alt_tag - the alt tag of the post
    @param excerpt - the excerpt of the post
    @param updated_at - the date the post was last updated
    @param category - the category of the post
    @param content - the content of the post
    @param created_at - the date the post was created
    @param likes - the likes of the post
    """

    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(max_length=250, populate_from="title", unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"is_staff": True},
        related_name="post_posts",
    )
    featured_image = CloudinaryField(
        folder="leannes_learners/blog_images/",
        transformation={
            "width": "800",
            "height": "600",
            "crop": "fill",
            "gravity": "face",
            "zoom": "0.5",
        },
        default="image/upload/leannes_learners/default_image/placeholder",
    )
    alt_tag = models.CharField(
        max_length=200, blank=True, verbose_name="image alternative text"
    )
    excerpt = models.TextField(
        blank=False,
        verbose_name="Eye Catching Excerpt - make someone want to read the article",
    )

    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    content = models.TextField(
        verbose_name="Post Content",
        blank=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blogPost_like", blank=True)

    def image_thumb(self):
        """
        Create a thumbnail for the image.
        @returns the thumbnail
        """
        return mark_safe(
            '<img src="{}" width="100" height="auto">'.format(self.featured_image.url)
        )

    image_thumb.short_discription = "image"
    featured_image.allow_tags = True

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        """
        returns the title of the post
        """
        return self.title

    def __str__(self):
        """
        Return the slug of the object.
        """
        return self.slug

    def number_of_likes(self):
        """
        Return the number of likes for a post.
        """
        return self.likes.count()

    def get_absolute_url(self):
        return "post/{}".format(self.slug)


class Comment(models.Model):
    """
    A class for the comments.
    """

    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    liked = models.ManyToManyField(User, blank=True, related_name="comments_liked")
    disliked = models.ManyToManyField(
        User, blank=True, related_name="comments_disliked"
    )
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, related_name="+"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        """
        Return a string representation of the comment.
        """
        return f"Comment {self.comment} by {self.name}"

    def number_of_comment_likes(self):
        """
        returns the number of likes for the comment
        """
        return self.liked.count()

    def number_of_comment_dislikes(self):
        """
        returns the number of likes for the comment
        """
        return self.disliked.count()

    @property
    def children(self):
        """
        returns child comments of a parent by created time
        """
        return Comment.objects.filter(parent=self).order_by("-created_at").all()

    @property
    def is_parent(self):
        """
        Check to see if the comment is a parent comment and return true
        """
        if self.parent is None:
            return True
        return False
