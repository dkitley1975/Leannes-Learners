from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, Carousel, CompanyDetails, TeachingHours, Instructors, Passplus, Service, Terms, Testimonial 


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin class for the About Us Page model
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

    search_fields = ['short_description', 'about-us',]
    list_filter = ('status',)
    actions = ['publish_About_us', 'unpublish_About_us']
    summernote_fields = ('about_us',)
    readonly_fields = ['image_thumb',]

    def publish_About_us(self, request, queryset):
        """
        Publish the About Us page.
        @param self - the current instance of the model being changed.
        @param request - the request object.
        @param queryset - the queryset of the model being changed.
        """
        queryset.update(status=True)

    def unpublish_About_us(self, request, queryset):
        """
        Unpublish the About Us page.
        @param self - the current page instance.
        @param request - the request object.
        @param queryset - the queryset of the current page.
        """
        queryset.update(status=False)


@admin.register(Carousel)
class CarouselAdmin(SummernoteModelAdmin):
    """
    Admin class for the Cauousel model
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
    summernote_fields = ('slide_text_description',)
    readonly_fields = ['image_thumb',]

    def include_in_carousel(self, request, queryset):
        """
        Update the include_in_carousel field to True for the queryset.
        @param self - the view itself, not used.
        @param request - the request itself, not used.
        @param queryset - the queryset to update.
        """
        queryset.update(include_in_carousel=True)


@admin.register(CompanyDetails)
class CompanyDetailsAdmin(admin.ModelAdmin):
    """
    Admin class for the company contact details model
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
    Admin class for the instructors model
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
        """
        Update the status of the instructor to True.
        @param self - the current instance of the instructor model.
        @param request - the request object.
        @param queryset - the queryset of the instructor model.
        """
        queryset.update(status=True)


@admin.register(Passplus)
class PassplusAdmin(SummernoteModelAdmin):
    """
    Admin class for the Pass Plus model
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
    summernote_fields = ('main_content',)
    readonly_fields = ['image_thumb',]

    def publish_Passplus(self, request, queryset):
        """
        Update the status of the selected Passplus objects to True.
        @param self - the current view instance.
        @param request - the current request.
        @param queryset - the selected Passplus objects.
        """
        queryset.update(status=True)

    def unpublish_Passplus(self, request, queryset):
        """
        Update the status of the selected Passplus to unpublish.
        @param self - the current view instance.
        @param request - the current request.
        @param queryset - the selected Passplus objects.
        """
        queryset.update(status=False)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Admin class for the services model
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
        """
        A function to be used in the admin interface to allow the user to select which services to include in the services page.
        @param self - the admin interface object itself.
        @param request - the request object itself.
        @param queryset - the queryset object itself.
        """
        queryset.update(featured=True)


@admin.register(Terms)
class TermsAdmin(SummernoteModelAdmin):
    """
    Admin class for the terms and conditions model
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
    summernote_fields = ('lead_content', 'main_content',)
    readonly_fields = ['image_thumb',]

    def publish_Terms(self, request, queryset):
        """
        Publish the selected terms.
        @param self - the view itself.
        @param request - the request itself.
        @param queryset - the queryset itself.
        """
        queryset.update(status=True)

    def unpublish_Terms(self, request, queryset):
        """
        Update the status of the terms to unpublish.
        @param self - the view itself.
        @param request - the request itself.
        @param queryset - the queryset itself.
        """
        queryset.update(status=False)


@admin.register(Testimonial)
class TestimonialAdmin(SummernoteModelAdmin):
    """
    Admin class for the testimonials Model
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
    summernote_fields = ('testimonial',)
    readonly_fields = ['image_thumb',]

    def publish_Testimonial(self, request, queryset):
        """
        Update the status of the testimonials to true.
        @param self - the current view instance.
        @param request - the current request.
        @param queryset - the testimonials to update.
        """
        queryset.update(status=True)


@admin.register(TeachingHours)
class TeachingHoursAdmin(admin.ModelAdmin):
    """
    Admin class for the Teaching Hours model.
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
