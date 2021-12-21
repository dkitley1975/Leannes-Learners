from django.contrib import admin 
from .models import Post, Comment, Services
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Post)

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_at')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_description', 'service_duration', 'price', 'featured', 'created_at')
    list_filter = ('service_name', 'featured')
    list_display = ('service_name', 'service_duration', 'price', 'featured')