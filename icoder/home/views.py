from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from icoder.settings import TEMPLATES
import os
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
        if len(searchKeyword) > 68 :
            fetched_blogs = Post.objects.none()
        else:
            fetched_title = Post.objects.all().filter(title__icontains=searchKeyword)
            fetched_content = Post.objects.all().filter(content__icontains=searchKeyword)
            fetched_blogs = fetched_title.union(fetched_content)

        if fetched_blogs.count() < 1: 
            messages.error(request, "No search result Found. Please refine your query!")
        

    params = {'fetched_blogs':fetched_blogs, 'query':searchKeyword}
    return render(request, 'home/search.html', params)

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # errors 
        # Throw error if user already exist  
        user_exist = User.objects.filter(username=username)

        if user_exist or pass1 != pass2:
            messages.error(request, 'User with this username already exist!')
            return redirect('home')
   
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your account has been sucessfully created.')

        return redirect('home')

        
    else:
        return HttpResponse('404 - Not Found')


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(username=loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else: 
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('home')
    return HttpResponse('Login')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Loggedout")
    return redirect('home')