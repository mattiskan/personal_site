from django.test import Client

from lxml import etree

from django.http import HttpResponse
from django.shortcuts import render

from blog.models import BlogEntry
from blog.api import EntryResource

def transform(xml, xsl):
    return etree.XSLT(etree.parse(xsl))(xml)

def index(request):
    feed_html = ''.join(
        etree.tostring(
            transform(
                EntryResource.as_xml(request, entry_id=entry.id),
                'blog/views/xsl/blog_feed.xsl'
            )
        )
        for entry in BlogEntry.objects.order_by('-id')
    )
    
    return render(request, 'feed.html', context={
        'feed_html': feed_html,
    })


def rss(request):
    rss_xml = etree.fromstring(Client().get('/blog/api/entry/').content)

    transformed_xml = transform(rss_xml, 'blog/views/xsl/rss_feed.xsl')

    return HttpResponse(etree.tostring(transformed_xml), content_type='text/xml')

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
