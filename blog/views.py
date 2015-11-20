from django.http import HttpResponse
from django.shortcuts import render

from models import BlogEntry


def index(request):
    entries = '<br/>'. join(entry.title for entry in BlogEntry.objects)
    
    return HttpResponse("Hello world<br/>" + entries)


def create(request):
    new_entry = BlogEntry(
        title = 'test title2',
        content = 'test content'
    )
    new_entry.save()  
    return HttpResponse("New blog entry added!")
