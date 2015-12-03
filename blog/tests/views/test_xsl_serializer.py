from lxml import etree
from blog.views.xsl_serializer import XslSerializer


def test_has_header():
    serializer = XslSerializer('path/to/stylesheet.xsl')

    xml_string = serializer.to_xml(object())

    xml_lines = xml_string.split('\n')
    assert xml_lines[0] == "<?xml version='1.0' encoding='utf-8'?>"
    assert xml_lines[1] == "<?xml-stylesheet type='text/xsl' href='path/to/stylesheet.xsl'?>"


    
def test_header_no_stylesheet():
    serializer = XslSerializer()

    xml_string = serializer.to_xml(object())

    xml_lines = xml_string.split('\n')
    assert xml_lines[0] == "<?xml version='1.0' encoding='utf-8'?>"
    assert not xml_lines[1].startswith("<?xml-stylesheet")
    
