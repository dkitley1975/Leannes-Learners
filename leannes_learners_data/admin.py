from django.contrib import admin 
from .models import Post
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
