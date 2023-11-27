from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import User

from .models import Post, User, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'pub_date', 'author']
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'text', 'created_at']

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)