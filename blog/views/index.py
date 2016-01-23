from django.test import Client

from lxml import etree

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

def subscribe(request):
    new_subscriber = EmailSubscribers(
        email = request.POST['email_address']
    )

    try:
        new_subscriber.save()
    except IntegrityError:
        return HttpResponse("already subscribed!", status=500)

    email_list = "<br>".join(str(subscriber.email) for subscriber in EmailSubscribers.objects.all())
    return HttpResponse(email_list)


def create(request):
    new_entry = BlogEntry(
        title = 'test title2',
        content = 'test content'
    )
    new_entry.save()
    return HttpResponse("New blog entry added!")
