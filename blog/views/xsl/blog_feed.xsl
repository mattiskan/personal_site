<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


  <xsl:template match="/">
    <div>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <xsl:template match="object">
    <a href="{resource_uri}"><h2><xsl:value-of select="id"/>: <xsl:value-of select="title"/></h2></a>
    <p><xsl:value-of select="content"/></p>
  </xsl:template>


  <!-- suppressed outputs -->
  <xsl:template match="offset"/>
  <xsl:template match="limit"/>
  <xsl:template match="total_count"/>
</xsl:stylesheet>
