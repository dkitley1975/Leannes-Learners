from django.contrib import admin
from .models import Blog, Comment, Services, HomeCarousel
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Blog)
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
        'slug',
        'author',
        'featured_image',
        'image_thumb',
        'alt_tag',
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

    search_fields = ['title', 'content', 'alt_tag']
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = ['publish_Blog']
    readonly_fields = ['image_thumb']

    def publish_Blog(self, request, queryset):
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
        'body',
        'blog',
        'created_at',
        'approved'
        )
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    """
    Establish the view in admin for the Services offered.
    Which fields to include in the:
    list/search views and how they are filtered.
    """
    list_display = (
        'service_name',
        'service_description',
        'service_duration',
        'price',
        'featured',
        'created_at'
        )
    list_filter = ('service_name', 'featured')


@admin.register(HomeCarousel)
class HomeCarouselAdmin(SummernoteModelAdmin):
    """
    Establish the view in admin for the Home Carousel.
    Which fields to include in the:
    list/search views and how they are filtered and
    create an action to include approve include in the carousel
    """
    list_display = (
        'slide_identifying_name',
        'slide_text_headline',
        'slide_text_description',
        'slide_image',
        'alt_tag',
        'include_in_carousel',
        )
    list_filter = ('slide_identifying_name', 'slide_text_headline',
                   'slide_text_description', 'slide_image',)
    search_fields = ('slide_identifying_name', 'slide_text_headline',
                     'slide_text_description', 'slide_image', 'alt_tag',)
    summernote_fields = ('slide_text_description',)
    actions = ['approve_comments']

    def include_in_carousel(self, request, queryset):
        queryset.update(include_in_carousel=True)
