from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()  # Fetch all posts
    return render(request, 'posts/post_list.html', {'posts': posts})
