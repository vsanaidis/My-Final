from django.contrib import admin
from .models import Post, Comment, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'note', 'description', 'created_at')
    search_fields = ('user__username', 'note__title', 'description')
    list_filter = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'text', 'created_at')
    search_fields = ('user__username', 'text')
    list_filter = ('created_at',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    search_fields = ('user__username',)
    list_filter = ('post',)
