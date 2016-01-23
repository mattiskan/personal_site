<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:rss="http://purl.org/rss/1.0/">

  <xsl:output method="html" version="1.0"
              encoding="utf-8" indent="yes"/>
  
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>  

  <xsl:template match="head/*[last()]">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
    <script>window.setTimeout(function() {window.location='/';}, 3000);</script>
  </xsl:template>

  <xsl:template match="header">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
    <div class="container">
      <div class="info">You will be automatically redirected in 3 seconds...</div>
    </div>
  </xsl:template>
  
</xsl:stylesheet>
