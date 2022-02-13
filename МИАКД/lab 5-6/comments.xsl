<?xml version="1.0" encoding="UTF-8" ?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h1>
                    <u>
                        Комментарии
                    </u>
                </h1>
                <table border="1">
                    <tr bgcolor="#ffff00">
                        <th>Id</th>
                        <th>Текст</th>
                        <th>Автор</th>
                        <th>Индекс видео</th>
                    </tr>
                    <xsl:for-each select="comments/comment">
                        <tr>
                            <td>
                                <xsl:value-of select="@id"/>
                            </td>
                            <td>
                                <xsl:value-of select="text"/>
                            </td>
                            <td>
                                <xsl:value-of select="author"/>
                            </td>
                            <td>
                                <xsl:value-of select="videoId"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
