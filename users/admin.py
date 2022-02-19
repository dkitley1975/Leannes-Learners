from django.contrib import admin
from .models import UserProfile
# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Publish the selected posts.
    @param request - the request object
    @param queryset - the queryset object
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

