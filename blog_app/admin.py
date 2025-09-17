from django.contrib import admin
from .models import Tweet, BlogPost
# Register your models here.

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'text', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['title', 'text', 'content']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['title', 'content']