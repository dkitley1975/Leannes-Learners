from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
from .models import About, Carousel, CompanyDetails, TeachingHours, Instructors, Passplus, Service, Terms, Testimonial 


# Register your models here.
@admin.register(About)
class AboutAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    """
    Unpublish the About Us page.
    @param self - the current page instance.
    @param request - the request object.
    @param queryset - the queryset of the current page.
    """
    fields = [
        'short_description',
        'about_us',
        'status',
    ]

    list_display = (
        'short_description',
        'status',
        'created_at',
        )

    search_fields = ['short_description', 'about-us',]
    list_filter = ('status',)
    actions = ['publish_About_us', 'unpublish_About_us']
    summernote_fields = ('about_us',)

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
class CarouselAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
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
class CompanyDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
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
class InstructorsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Admin class for the instructors model
    """
    fields = [
        'name',
        'image_thumb',
        'instructor_image',
        'alt_tag',
        'about',
        'status',
        
    ]

    list_display = (
        'name',
        'about',
        'status',
        'created_at',
        'image_thumb',
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
class PassplusAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    """
    Admin class for the Pass Plus model
    """
    fields = [
        'short_description',
        "lead_content",
        'main_content',
        'focus_image',
        'alt_tag',
        'status',
    ]

    list_display = (
        'short_description',
        'status',
        'created_at',
        )

    search_fields = ['short_description', 'lead_content', 'main_content', 'alt_tag',]
    list_filter = ('status', 'created_at',)
    actions = ['publish_Passplus', 'unpublish_Passplus']
    summernote_fields = ('main_content',)

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
class ServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """
    This is the admin page for the ImportExportModel. It allows the user to see the           
    model's name, the number of parameters, and the accuracy of the model.
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
        A custom filter for the admin site. This function will only return objects that are in the Services table.
        @param request - the request object           
        @param queryset - the queryset object           
        @return the queryset object           
        """
        queryset.update(featured=True)


@admin.register(Terms)
class TermsAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    """
    The fields for the admin page for the ImportExportModelAdmin and the SummernoteModelAdmin.
    """
    fields = [
        'lead_content',
        'main_content',
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
class TestimonialAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    """
    Update the status of the testimonials to true.
    @param self - the current view instance.
    @param request - the current request.
    @param queryset - the testimonials to update.
    """
    fields = [
        'name',
        'testimonial_image',
        'alt_tag',
        'testimonial',
        'status',
    ]

    list_display = (
        'name',
        'testimonial',
        'status',
        'created_at',
        )

    search_fields = ['name', 'testimonial', 'alt_tag',]
    list_filter = ('status', 'created_at')
    actions = ['publish_Testimonial',]
    summernote_fields = ('testimonial',)

    def publish_Testimonial(self, request, queryset):
        """
        Publish the testimonials that are selected.
        @param request - the request object
        @param queryset - the testimonials that are selected
        """
        queryset.update(status=True)


@admin.register(TeachingHours)
class TeachingHoursAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """
    This is a custom admin class for the ImportExportModel class. It allows us to import and export models.
    @param ImportExportModelAdmin - the admin class for the ImportExportModel class
    @param admin.ModelAdmin - the admin class for the Model class
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
