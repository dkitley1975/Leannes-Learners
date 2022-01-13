from django.contrib import admin
from .models import About, Blog, Carousel, Comment, CompanyDetails, TeachingHours, Instructors, Passplus, Service, Testimonial 
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Establish the view in admin for About content page.
    Which fields to include in the:
    list/search views, how they are filtered,
    which are prepopulated and
    creates an action to include approve About.
    """
    fields = [
        'short_description',
        'about_us',
        'background_image',
        'image_thumb',
        'status',
    ]

    list_display = (
        'short_description',
        'image_thumb',
        'status',
        'created_at',
        )

    search_fields = ['short_description', 'about_us',]
    list_filter = ('status',)
    summernote_fields = ('about_us',)
    actions = ['publish_About_us', 'Unpublish_About_us']
    readonly_fields = ['image_thumb',]

    def publish_About_us(self, request, queryset):
        queryset.update(status=True)

    def Unpublish_About_us(self, request, queryset):
        queryset.update(status=False)


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


@admin.register(Instructors)
class InstructorsAdmin(SummernoteModelAdmin):
    """
    Establish the view in admin for the Driving Instructors.
    Which fields to include in the:
    list/search views, how they are filtered,
    which are prepopulated and
    creates an action to include activate Driving Instructors.
    """
    fields = [
        'name',
        'instructor_image',
        'image_thumb',
        'alt_tag',
        'about',
        'status',
    ]

    list_display = (
        'image_thumb',
        'name',
        'about',
        'status',
        'created_at',
        )

    search_fields = ['name',]
    list_filter = ('status',)
    actions = ['publish_Instructor',]
    readonly_fields = ['image_thumb',]

    def publish_Instructor(self, request, queryset):
        queryset.update(status=True)


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
        'short_description',
        "lead_content",
        'main_content',
        'focus_image',
        'alt_tag',
        'background_image',
        'image_thumb',
        'status',
    ]

    list_display = (
        'image_thumb',
        'short_description',
        'status',
        'created_at',
        )

    search_fields = ['short_description', 'lead_content', 'main_content', 'alt_tag',]
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


@admin.register(CompanyDetails)
class CompanyDetailsAdmin(admin.ModelAdmin):
    """
    Establish the view in admin for the Company Details.
    Which fields to include in the:
    list/search views.
    """
    fields = [
        'phone',
        'email',
        'social_media_name',
        'social_media_link',
        'social_media_image',
        'social_media_name_2',
        'social_media_link_2',
        'social_media_image_2',
        'social_media_name_3',
        'social_media_link_3',
        'social_media_image_3',
        'social_media_name_4',
        'social_media_link_4',
        'social_media_image_4',
        'background_image',
        'image_thumb',
    ]

    list_display = (
        'id', 'phone',
        'social_media_name',
        'social_media_name_2',
        'social_media_name_3',
        'social_media_name_4',
        'image_thumb',
        )

    search_fields = ['phone', 'email',]
    list_filter = ('phone', 'email',)
    readonly_fields = ['image_thumb',]


@admin.register(TeachingHours)
class TeachingHoursAdmin(admin.ModelAdmin):
    """
    Establish the view in admin for the Contact Details.
    Which fields to include in the:
    list/search views.
    """
    fields = [
        'day',
        'start_time',
        'finish_time'
    ]

    list_display = (
        'day',
        'start_time',
        'finish_time'
        )

    search_fields = ['day', 'email']
