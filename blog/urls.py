from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from views import index, edit_entry
from api import EntryResource

entry_resource = EntryResource()

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^mobile/$', index.mobile, name='mobile'),
    url(r'^create/$', edit_entry.create, name='create'),
    url(r'^edit/(?P<entry_id>[0-9]+)/$', edit_entry.edit, name='edit'),
    url(r'^search$', index.search, name='search'),
    url(r'^subscribe$', index.subscribe, name='subscribe'),
    url(r'^entry/(?P<entry_id>[0-9]+)/$', index.entry, name='entry'),
    url(r'^entry/(?P<entry_id>[0-9]+)/reply-count/$', index.reply_count, name='reply_count'),
    url(r'^rss/$', index.rss, name='rss'),
    url(r'^api/', include(entry_resource.urls)),
]

urlpatterns += staticfiles_urlpatterns()
