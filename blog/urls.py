from django.conf.urls import include, url

from . import views
from api import EntryResource

entry_resource = EntryResource()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='index'),

    url(r'^api/', include(entry_resource.urls)),
]
