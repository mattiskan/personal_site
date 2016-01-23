from django.test import Client

from lxml import etree

from django.http import HttpResponse
from django.shortcuts import render

from blog.models import BlogEntry
from blog.api import EntryResource



def transform(xsl):
    def wrap(function):
        def transformed(*args, **kwargs):
            output = etree.fromstring(''.join(function(*args, **kwargs)))
            return HttpResponse(etree.XSLT(etree.parse(xsl))(output))
        return transformed
    return wrap


def index(request):
    return render(request, 'feed.html', context={
        'entries': list(BlogEntry.objects.order_by('-id')),
    })

@transform('blog/views/xsl/rss_feed.xsl')
def rss(request):
    return HttpResponse(Client().get('/blog/api/entry/').content)

@transform('blog/views/xsl/id.xsl')
def entry(request, entry_id):
    be = BlogEntry.objects.get(pk=entry_id)

    return render(request, 'entry.html',context={
        'title': be.title,
        'entry': be,
    })    

def create(request):
    new_entry = BlogEntry(
        title = 'test title2',
        content = 'test content'
    )
    new_entry.save()
    return HttpResponse("New blog entry added!")
