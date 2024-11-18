from django.shortcuts import render, HttpResponse
from home.models import Contact
from icoder.settings import TEMPLATES
import os

# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def contact(request):
    print('Hello')
    if request.method == 'POST':
        name = request.POST.get('name', 'abcd')
        email = request.POST.get('email', 'abcd')
        phoneno = request.POST.get('phoneno', 'abcd')
        content = request.POST.get('content', 'abcd')

        try:
            new_contact_entry = Contact(name=name, email=email, phoneno=phoneno, content=content)
            new_contact_entry.save()
        except Exception as e:
            print(e)
            return render(request, 'home/contact.html')

    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')
