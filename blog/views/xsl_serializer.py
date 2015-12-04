from lxml import etree
from tastypie.serializers import Serializer


class XslSerializer(Serializer):

    supported_formats = ('xml')
    
    def __init__(self, stylesheet=None):
        self.stylesheet = stylesheet

    
    def to_xml(self, data, options=None):
        original_xml = super(XslSerializer, self).to_etree(data, options)
        no_header_xml_str = etree.tostring(original_xml, xml_declaration=False, encoding='utf-8')

        header = '<?xml version="1.0" encoding="utf-8"?>\n'
        if self.stylesheet:
            header += '<?xml-stylesheet type="text/xsl" href="{}"?>\n'.format(self.stylesheet)


        return header + no_header_xml_str
