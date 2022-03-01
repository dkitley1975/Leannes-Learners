from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportActionMixin

from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin



# Register your models here.

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    """
    Establish the view in admin for the Categories.
    .
    """
    list_display = ['name',]
    list_filter = ['name',]
    search_fields = ['name',]


@admin.register(Post)
class BlogAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
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
        'likes',
    ]

    list_display = (
        'image_thumb',
        'title',
        'slug',
        'category',
        'created_at',
        )

    search_fields = ['title', 'content', 'alt_tag',]
    list_filter = ('category','created_at')
    summernote_fields = ('content',)
    readonly_fields = ['image_thumb', 'slug']



@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
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
        )
    list_filter = ('name', 'created_at')
    search_fields = ('name', 'comment')


