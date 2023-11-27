from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

# Create your views here.
def index(request):
   return HttpResponse("Hi Arlinda, you are a user")

def post_list(request):
    posts = Post.objects.all()  # Fetch all posts
    return render(request, 'posts/post_list.html', {'posts': posts})