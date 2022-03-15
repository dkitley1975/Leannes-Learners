from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import UserProfile
# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Publish the selected posts.
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

    search_fields = ['user', 'user_bio']
    readonly_fields = ['image_thumb']

    def publish_Post(self, request, queryset):
        """
        Update the status of the post to published.
        """
        queryset.update(status=True)
