from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.

def blogHome(request):
    all_blogs = Post.objects.all()
    params = {'all_blogs': all_blogs }
    return render(request, 'blog/blogHome.html', params)

def blogPost(request, slug):
    fetch_blog = Post.objects.filter(slug = slug)[0]
    params = {'fetch_blog': fetch_blog}
    return render(request, 'blog/blogPost.html', params)
