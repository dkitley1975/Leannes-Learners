from django.contrib import admin
from .models import UserProfile
# Register your models here.


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

