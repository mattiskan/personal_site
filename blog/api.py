from tastypie.resources import ModelResource
from models import BlogEntry


class EntryResource(ModelResource):
    class Meta:
        queryset = BlogEntry.objects.all()
        resource_name = 'entry'                    
