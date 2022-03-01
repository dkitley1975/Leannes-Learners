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
	name = models.CharField(max_length=50)
	class Meta:
		ordering = ["name"]
		verbose_name = "Category"
		verbose_name_plural = "Categories"
	def __str__(self):
		"""
		returns the name of the category 
		"""
		return self.name


class Post(models.Model):
	"""
	The Post model for the blog. This is the model that will be used to store the blog posts.
	@param title - the title of the post
	@param slug - the slug of the post
	@param author - the author of the post
	@param featured_image - the featured image of the post
	@param alt_tag - the alt tag of the post
	@param excerpt - the excerpt of the post
	@param updated_at - the updated at of the post
	@param category - the category of the post
	@param content - the content of the post
	@param created_at - the created at of the post
	@param likes - the likes of the post
	"""
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
		"""
		Create a thumbnail for the image.
		@returns the thumbnail
		"""
		return mark_safe('<img src="{}" width="100" height="auto">'.format(
			self.featured_image.url))
	image_thumb.short_discription = "image"
	featured_image.allow_tags = True

	class Meta:
		ordering = ["-created_at"]
		verbose_name = "Post"
		verbose_name_plural = "Posts"

	def __str__(self):
		"""
		returns the title of the post 
		"""
		return self.title

	def __str__(self):
		"""
		returns the slug of the post 
		"""
		return self.slug

	def number_of_likes(self):
		"""
		returns the number of likes for the post 
		"""
		return self.likes.count()

	def get_absolute_url(self):
		return ('post/{}'.format(self.slug))


class Comment(models.Model):
	"""
	The comment model. This is the model that is used to store the comments.
	@param comment - the comment itself
	@param created_at - the date and time the comment was created
	@param name - the user who created the comment
	@param liked - the users who liked the comment
	@param disliked - the users who disliked the comment
	@param parent - the parent comment
	@param post - the post the comment is associated with
	"""
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	# user_profile_image = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='avatar')
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
		"""
		Return a string representation of the comment.
		@returns the string representation of the comment.
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
		return Comment.objects.filter(parent=self).order_by('-created_at').all()

	@property
	def is_parent(self):
		""" 
		Check to see if the comment is a parent comment and return true
		"""
		if self.parent is None:
			return True
		return False
