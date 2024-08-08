from django.contrib import admin
from .models import PostModel


class PostModelAdmin(admin.ModelAdmin):
    search_fields = ['post_title']
    list_display = ['post_title', 'post_author', 'post_created', 'post_likes_count', 'post_file']

    def post_likes_count(self, obj):
        return obj.post_likes.count()

    post_likes_count.short_description = 'Post Likes'


admin.site.register(PostModel, PostModelAdmin)
