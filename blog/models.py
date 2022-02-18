# from ast import Return
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.safestring import mark_safe
# from django.urls import reverse
from autoslug import AutoSlugField
# from django_summernote.widgets import SummernoteWidget


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
	"""	Model for the Category list """	
	name = models.CharField(max_length=50)
	class Meta:
		ordering = ["name"]
		verbose_name = "Category"
		verbose_name_plural = "Categories"
	def __str__(self):
		return self.name


class Post(models.Model):
	"""	Model for the Blog Posts """	
	title = models.CharField(max_length=200, unique=True)
	slug = AutoSlugField(max_length=250, populate_from='title', unique=True)
	author = models.ForeignKey(
		User, on_delete=models.CASCADE, related_name="post_posts"
	)
	featured_image = CloudinaryField(
		folder='leannes_learners/blog_images/',
		transformation={
			'width': '400',
			'height': '300',
			'crop': 'fill',
			'gravity': 'face',
			'zoom': '0.5'
			},
		default='image/upload/leannes_learners/default_image/placeholder')
	alt_tag = models.CharField(max_length=200, blank=True,
		verbose_name='Describe the image for the blind')
	excerpt = models.TextField(blank=False,
		verbose_name='Eye Catching Excerpt - make someone want to read the article')

	updated_at = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
	content = models.TextField(verbose_name='Post Content', blank=False,)
	created_at = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(
		User, related_name='blogPost_like', blank=True)

	def image_thumb(self):
		""" This creates a thumbnail image of the current uploaded image """
		return mark_safe('<img src="{}" width="100" height="auto">'.format(
			self.featured_image.url))
	image_thumb.short_discription = "image"
	featured_image.allow_tags = True

	class Meta:
		ordering = ["-created_at"]
		verbose_name = "Post"
		verbose_name_plural = "Posts"

	def __str__(self):
		return self.title

	def __str__(self):
		return self.slug

	def number_of_likes(self):
		return self.likes.count()

	def get_absolute_url(self):
		return ('post/{}'.format(self.slug))


class Comment(models.Model):
	"""	Model for the Post Comments """
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	liked = models.ManyToManyField(User, blank=True, 
		related_name="comments_liked")
	disliked = models.ManyToManyField(User, blank=True,
		related_name="comments_disliked")
	parent = models.ForeignKey('self', on_delete=models.CASCADE, 
		blank=True, null=True, related_name='+')								  
	post = models.ForeignKey(Post, on_delete=models.CASCADE, 
		related_name="comments")

	class Meta:
		ordering = ["created_at"]
		verbose_name = "Comment"
		verbose_name_plural = "Comments"

	def __str__(self):
		return f"Comment {self.comment} by {self.name}"


	@property
	def children(self):
		""" returns child comments of a parentby created time """
		return Comment.objects.filter(parent=self).order_by('-created_at').all()

	@property
	def is_parent(self):
		""" Check to see if the comment is a parent comment and return true """
		if self.parent is None:
			return True
		return False
