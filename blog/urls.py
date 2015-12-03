from django.conf.urls import include, url

from views import index
from api import EntryResource

entry_resource = EntryResource()

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^create$', index.create, name='index'),

    url(r'^api/', include(entry_resource.urls)),
]
