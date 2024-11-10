from django.shortcuts import render, HttpResponse

# Create your views here.

def blogHome(request):
    return HttpResponse('This is blogHome page.')

def blogPost(request, slug):
    return HttpResponse(f'This is blog {slug} page.')