from lxml import etree

from django.http import HttpResponse
from django.shortcuts import render

from blog.models import BlogEntry
from blog.api import EntryResource



transform = etree.XSLT(etree.parse('blog/views/xsl/blog_feed.xsl'))

def index(request):
    return HttpResponse(
        '<!DOCTYPE html><html><body>' +
        ''.join(
            etree.tostring(transform(EntryResource.as_xml(request, entry_id=entry.id)))
            for entry in BlogEntry.objects.all()
        )
        + '</body></html>'
    )


def create(request):
    new_entry = BlogEntry(
        title = 'test title2',
        content = 'test content'
    )
    new_entry.save()  
    return HttpResponse("New blog entry added!")
