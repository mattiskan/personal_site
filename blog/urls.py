from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from views import index
from api import EntryResource

entry_resource = EntryResource()

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^create$', index.create, name='create'),
    url(r'^entry/(?P<entry_id>[0-9]+)/$', index.entry, name='entry'),
    url(r'^rss/$', index.rss, name='rss'),
    url(r'^api/', include(entry_resource.urls)),
]

urlpatterns += staticfiles_urlpatterns()
