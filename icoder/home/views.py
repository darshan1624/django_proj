from django.shortcuts import render, HttpResponse
from home.models import Contact
from icoder.settings import TEMPLATES
import os
from django.contrib import messages
from blog.models import Post

# Create your views here.

def home(request):
    all_blogs = Post.objects.all()
    params = {'popular_blogs': all_blogs[:2]}
    return render(request, 'home/home.html', params)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'abcd')
        email = request.POST.get('email', 'abcd')
        phoneno = request.POST.get('phoneno', 'abcd')
        content = request.POST.get('content', 'abcd')

        try:
            if len(content) < 4:
                messages.error(request, 'Error: Please enter your query properly.')
            else:
                new_contact_entry = Contact(name=name, email=email, phoneno=phoneno, content=content)
                new_contact_entry.save()
                messages.success(request, 'Query Submitted successfully.')

        except Exception as e:
            print(e)
            return render(request, 'home/contact.html')

    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')

def search(request):
    if request.method == 'GET':
        searchKeyword = request.GET.get('search', '')
        fetched_blogs = Post.objects.all().filter(title__icontains=searchKeyword)

    params = {'fetched_blogs':fetched_blogs}
    return render(request, 'home/search.html', params)
