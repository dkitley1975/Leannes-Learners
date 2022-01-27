from django.contrib import admin
from .models import About, Carousel, CompanyDetails, TeachingHours, Instructors, Passplus, Service, Terms, Testimonial 
from tinymce.models import HTMLField


# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    Establish the view in admin for About content page.
    Which fields to include in the:
    list/search views, how they are filtered,
    which are prepopulated and
    creates an action to include approve About.
    """
    fields = [
        'short_description',
        'about-us',
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

    search_fields = ['short_description', 'about-us',]
    list_filter = ('status',)
    actions = ['publish_About_us', 'unpublish_About_us']
    readonly_fields = ['image_thumb',]

    def publish_About_us(self, request, queryset):
        queryset.update(status=True)

    def unpublish_About_us(self, request, queryset):
        queryset.update(status=False)


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
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
    actions = ['include_in_carousel',]
    readonly_fields = ['image_thumb',]

    def include_in_carousel(self, request, queryset):
        queryset.update(include_in_carousel=True)


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
    ]

    list_display = (
        'id', 'phone',
        'social_media_name',
        'social_media_name_2',
        'social_media_name_3',
        'social_media_name_4',
        )

    search_fields = ['phone', 'email',]
    list_filter = ('phone', 'email',)


@admin.register(Instructors)
class InstructorsAdmin(admin.ModelAdmin):
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
class PassplusAdmin(admin.ModelAdmin):
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
    actions = ['publish_Passplus', 'unpublish_Passplus']
    readonly_fields = ['image_thumb',]

    def publish_Passplus(self, request, queryset):
        queryset.update(status=True)

    def unpublish_Passplus(self, request, queryset):
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


@admin.register(Terms)
class TermsAdmin(admin.ModelAdmin):
    """
    Establish the view in admin for Terms and Conditions content page.
    Which fields to include in the:
    list/search views, how they are filtered,
    which are prepopulated and
    creates an action to include approve terms.
    """
    fields = [
        'lead_content',
        'main_content',
        'background_image',
        'image_thumb',
        'status',
    ]

    list_display = (
        'status',
        'created_at',
        'lead_content',
        )

    search_fields = ['lead_content', 'main_content']
    list_filter = ('status', 'created_at',)
    actions = ['publish_Terms', 'unpublish_Terms']
    readonly_fields = ['image_thumb',]

    def publish_Terms(self, request, queryset):
        queryset.update(status=True)

    def unpublish_Terms(self, request, queryset):
        queryset.update(status=False)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
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
    actions = ['publish_Testimonial',]
    readonly_fields = ['image_thumb',]

    def publish_Testimonial(self, request, queryset):
        queryset.update(status=True)


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
