from tastypie.resources import ModelResource
from models import BlogEntry
from views.xsl_serializer import XslSerializer


class EntryResource(ModelResource):
    class Meta:
        queryset = BlogEntry.objects.all()
        resource_name = 'entry'                    

        serializer = XslSerializer(stylesheet=None)
