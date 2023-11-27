from .models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'pub_date', 'author']