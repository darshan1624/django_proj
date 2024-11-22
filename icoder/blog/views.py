from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.

def blogHome(request):
    all_blogs = Post.objects.all()
    params = {'all_blogs': all_blogs }
    return render(request, 'blog/blogHome.html', params)

def blogPost(request, slug):
    return render(request, 'blog/blogPost.html')
