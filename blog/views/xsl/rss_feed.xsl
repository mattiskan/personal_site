<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:rss="http://purl.org/rss/1.0/">

  <xsl:template match="/">
    <rss version="2.0">
      <channel>
        <title>Blog RSS</title>
        <description>RSS feed</description>
        <link>http://192.168.99.100:8000/blog/rss</link>
 
        <xsl:apply-templates/>

      </channel>
    </rss>
  </xsl:template>

      <xsl:template match="object">
        <item>
          <title>
            <xsl:value-of select="title"/>
          </title>
          <description>
            <xsl:value-of select="content"/>
          </description>
          <link>
            http://192.168.99.100:8000<xsl:value-of select="resource_uri"/>
          </link>
        </item>
      </xsl:template>

      <!-- suppressed outputs -->
      <xsl:template match="id"/>
      <xsl:template match="resource_uri"/>
      <xsl:template match="offset"/>
      <xsl:template match="limit"/>
      <xsl:template match="total_count"/>
</xsl:stylesheet>
