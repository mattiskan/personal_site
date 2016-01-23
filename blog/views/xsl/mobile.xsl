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
  
  <xsl:template match="/html/body/header/ul">
    <div class="container">
    <select class="hfill" onChange="window.location=this.value">
      <xsl:apply-templates/>
    </select>
    </div>
  </xsl:template>

  <xsl:template match="/html/body/header/ul/li">
    <option value="{./a/@href}">
      <xsl:value-of select="."/>
    </option>
  </xsl:template>
  
</xsl:stylesheet>
