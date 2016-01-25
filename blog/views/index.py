import json
import urllib2
import time
from django.test import Client

from lxml import etree
from pyquery import PyQuery as pq

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
    be = get_object_or_404(BlogEntry, id=entry_id)
    url = 'http://discourse.mattiskan.se/c/blog.json'

    category = json.loads(urllib2.urlopen(url).read())

    for topic in category['topic_list']['topics']:        
        topic_data = json.loads(urllib2.urlopen(
            'http://discourse.mattiskan.se/t/%d.json' % topic['id']
        ).read())['details']

        
        if 'links' in topic_data:
            if topic_data['links'][0]['url'][-4:] == '/%s/' % entry_id:
                return HttpResponse(int(topic['posts_count']) - 1)
        time.sleep(0.5)


def search(request):
    query = request.GET['query']
    
    search_results = [
        be for be in BlogEntry.objects.order_by('-id')
        if query.lower() in (be.title + be.content).lower()
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

