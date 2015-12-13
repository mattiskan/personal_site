from lxml import etree

from django.http import HttpResponse
from django.shortcuts import render

from blog.models import BlogEntry
from blog.api import EntryResource

def transform(xml):
    return etree.XSLT(etree.parse('blog/views/xsl/blog_feed.xsl'))(xml)

def index(request):
    feed_html = ''.join(
        etree.tostring(transform(EntryResource.as_xml(request, entry_id=entry.id)))
        for entry in BlogEntry.objects.order_by('-id')
    )
    
    return render(request, 'feed.html', context={
        'feed_html': feed_html,
    })

def entry(request, entry_id):
    entry_html = etree.tostring(
        transform(
            EntryResource.as_xml(request, entry_id=entry_id)
        )
    )

    return render(request, 'entry.html',context={
        'entry_html': entry_html,
    })    

def create(request):
    new_entry = BlogEntry(
        title = 'test title2',
        content = 'test content'
    )
    new_entry.save()
    return HttpResponse("New blog entry added!")
