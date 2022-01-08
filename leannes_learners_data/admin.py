from django.contrib import admin
from .models import Blog, Comment, Testimonial, Service, Carousel, Passplus
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

    search_fields = ['title', 'content', 'alt_tag',]
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = ['publish_Blog',]
    readonly_fields = ['image_thumb',]

    def publish_Blog(self, request, queryset):
        queryset.update(status=True)


@admin.register(Carousel)
class CarouselAdmin(SummernoteModelAdmin):
    """
    Establish the view in admin for the Home Carousel.
    Which fields to include in the:
    list/search views and how they are filtered and
    create an action to include approve include in the carousel
    """
    fields = [
        'slide_identifying_name',
        'slide_text_headline',
        'slide_text_description',
        'slide_image',
        'image_thumb',
        'alt_tag',
        'include_in_carousel',
    ]
    list_display = (
        'image_thumb',
        'slide_identifying_name',
        'slide_text_headline',
        'slide_text_description',
        'alt_tag',
        'include_in_carousel',
        )
    list_filter = ('slide_identifying_name', 'slide_text_headline',
                   'slide_text_description', 'slide_image',)
    search_fields = ('slide_identifying_name', 'slide_text_headline',
                     'slide_text_description', 'slide_image', 'alt_tag',)
    summernote_fields = ('slide_text_description',)
    actions = ['include_in_carousel',]
    readonly_fields = ['image_thumb',]

    def include_in_carousel(self, request, queryset):
        queryset.update(include_in_carousel=True)


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
    actions = ['approve_comments',]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Passplus)
class PassplusAdmin(SummernoteModelAdmin):
    """
    Establish the view in admin for Passplus content page.
    Which fields to include in the:
    list/search views, how they are filtered,
    which are prepopulated and
    creates an action to include approve Testimonials.
    """
    fields = [
        'name',
        "lead_content",
        'main_content',
        'focus_image',
        'focus_image_alt_tag',
        'background_image',
        'image_thumb',
        'status',
    ]

    list_display = (
        'image_thumb',
        'name',
        'status',
        'created_at',
        )

    search_fields = ['name', 'lead_content', 'main_content', 'alt_tag',]
    list_filter = ('status', 'created_at',)
    summernote_fields = ('main_content',)
    actions = ['publish_Passplus', 'Unpublish_Passplus']
    readonly_fields = ['image_thumb',]

    def publish_Passplus(self, request, queryset):
        queryset.update(status=True)

    def Unpublish_Passplus(self, request, queryset):
        queryset.update(status=False)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Establish the view in admin for the Service offered.
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

    def include_in_Services(self, request, queryset):
        queryset.update(featured=True)


@admin.register(Testimonial)
class TestimonialAdmin(SummernoteModelAdmin):
    """
    Establish the view in admin for the Testimonials.
    Which fields to include in the:
    list/search views, how they are filtered,
    which are prepopulated and
    creates an action to include approve Testimonials.
    """
    fields = [
        'name',
        'testimonial_image',
        'image_thumb',
        'alt_tag',
        'testimonial',
        'status',
    ]

    list_display = (
        'image_thumb',
        'name',
        'testimonial',
        'status',
        'created_at',
        )

    search_fields = ['name', 'testimonial', 'alt_tag',]
    list_filter = ('status', 'created_at')
    summernote_fields = ('testimonial',)
    actions = ['publish_Testimonial',]
    readonly_fields = ['image_thumb',]

    def publish_Testimonial(self, request, queryset):
        queryset.update(status=True)

