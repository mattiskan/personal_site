<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <div class="blog-entry">
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <xsl:template match="object">
    <a href="/blog/entry/{id}/">
      <h2 class="title">
        <xsl:value-of select="title"/>
      </h2>
    </a>
    <p class="content"><xsl:value-of select="content"/></p>
  </xsl:template>


  <!-- suppressed outputs -->
  <xsl:template match="offset"/>
  <xsl:template match="limit"/>
  <xsl:template match="total_count"/>
</xsl:stylesheet>
