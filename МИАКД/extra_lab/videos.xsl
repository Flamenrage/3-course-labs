<?xml version="1.0" encoding="UTF-8" ?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h1>
                    <u>
                        Видео-ролики
                    </u>
                </h1>
                <table border="1">
                    <tr bgcolor="#ffff00">
                        <th>Id</th>
                        <th>Название</th>
                        <th>Описание</th>
                        <th>Длительность в минутах</th>
                    </tr>
                    <xsl:for-each select="videos/video">
                        <tr>
                            <td>
                                <xsl:value-of select="@id"/>
                            </td>
                            <td>
                                <xsl:value-of select="name"/>
                            </td>
                            <td>
                                <xsl:value-of select="description"/>
                            </td>
                            <td>
                                <xsl:value-of select="lasting"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
