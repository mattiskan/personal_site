from lxml import etree

from tastypie.resources import ModelResource
from models import BlogEntry
from views.xsl_serializer import XslSerializer


class EntryResource(ModelResource):
    class Meta:
        queryset = BlogEntry.objects.all()


        resource_name = 'entry'

    def determine_format(self, request):
        return 'application/xml' # makes ?format=xml redundant

    @classmethod
    def as_xml(cls, request, entry_id):
        """returns etree.XML object of entry.id"""

        er = cls()
        bundle = er.full_dehydrate(
            er.build_bundle(
                request=request,
                obj=er.obj_get(er.build_bundle(request=request), id=entry_id)
            )
        )
        return etree.fromstring(er.serialize(request, bundle, 'application/xml'))
