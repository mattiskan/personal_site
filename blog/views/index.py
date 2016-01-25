from django.test import Client

from lxml import etree
from pyquery import PyQuery as pq

from django.http import HttpResponse
from django.shortcuts import render
from django.db import IntegrityError

from blog.models import BlogEntry, EmailSubscribers
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


@transform('blog/views/xsl/mobile.xsl')
def mobile(request):
    return index(request)


@transform('blog/views/xsl/rss_feed.xsl')
def rss(request):
    return HttpResponse(Client().get('/blog/api/entry/').content)


def entry(request, entry_id):
    be = BlogEntry.objects.get(pk=entry_id)

    return render(request, 'entry.html',context={
        'title': be.title,
        'entry': be,
    })

def reply_count(request, entry_id):
    url = 'http://discourse.mattiskan.se/t/' + entry_id
    resp = pq(url=url)
    position = int(resp('span[itemprop=position]')[-1].text[1:])
    return HttpResponse(str(position - 1))


def search(request):
    query = request.GET['query']
    
    search_results = [
        be for be in BlogEntry.objects.order_by('-id')
        if query in be.title + be.content
    ]
    
    return render(request, 'feed.html', context={
        'entries': search_results,
    })


@transform('blog/views/xsl/redirect.xsl')
def subscribe(request):
    new_subscriber = EmailSubscribers(
        email = request.POST['email_address']
    )

    try:
        new_subscriber.save()
    except IntegrityError:
        return render(request, 'response.html', {'message': '<p>You were already subscribed!</p>'})

    return render(request, 'response.html', {'message': '<p>You have subscribed!</p>'})

