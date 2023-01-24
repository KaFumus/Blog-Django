from django.contrib import admin
from .models import Post

admin.site.register(Post)

# @admin.register(Post)
# class PostListAdmin(admin.ModelAdmin):
#     display_list = ['title', 'hashtags', 'author', 'publish', 'status']
#     filter_list = ['status', 'created', 'publish', 'author']
    