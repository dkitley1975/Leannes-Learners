from django.contrib import admin
from .models import Post, Comment, Category, UserProfile
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import strip_tags


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Establish the view in admin for the Categories.
    .
    """
    list_display = ['name',]
    list_filter = ['name',]
    search_fields = ['name',]


@admin.register(Post)
class BlogAdmin(SummernoteModelAdmin):
    """
    Establish the view in admin for the Blog.
    Which fields to include in the:
    list/search views, how they are filtered,
    which are prepopulated and
    creates an action to include approve Blogs.
    """
    fields = [
        'title',
        'author',
        'featured_image',
        'image_thumb',
        'alt_tag',
        'category',
        'excerpt',
        'content',
        'status',
        'likes',
    ]

    list_display = (
        'image_thumb',
        'title',
        'slug',
        'status',
        'created_at',
        )

    search_fields = ['title', 'content', 'alt_tag',]
    list_filter = ('status', 'created_at')
    actions = ['publish_Post',]
    summernote_fields = ('content',)
    readonly_fields = ['image_thumb', 'slug']

    def publish_Post(self, request, queryset):
        queryset.update(status=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Establish the view in admin for the Comments.
    Which fields to include in the:
    list/search views, how they are filtered and
    creates an action to include approve Blogs.
    """
    list_display = (
        'name',
        'comment',
        'created_at',
        'approved'
        )
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments',]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Establish the view in admin for the User Profile.
    Which fields to include in the:
    list/search views, how they are filtered,
    which are prepopulated.
    """
    fields = [
        'user',
        'user_bio',
        'user_profile_image',
        'user_facebook_url',
        'user_twitter_url',
        'user_linkedin_url',
        'user_website_url',
    ]
    
    list_display = (
        'image_thumb',
        'user',
        'user_bio',
        )

    search_fields = ['user', 'user_bio',]
    readonly_fields = ['image_thumb',]


    def publish_Post(self, request, queryset):
        queryset.update(status=True)

