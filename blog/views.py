from django.http import HttpResponse
from django.shortcuts import render

from models import BlogEntry


def index(request):
    entries = ''.join('<p class="blog-entry">' + entry.title + '</p>' for entry in BlogEntry.objects)
    
    return HttpResponse(entries)


def create(request):
    new_entry = BlogEntry(
        title = 'test title2',
        content = 'test content'
    )
    new_entry.save()  
    return HttpResponse("New blog entry added!")
