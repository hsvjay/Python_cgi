#!/usr/bin/python

import cgi
import cgitb;cgitb.enable()
form = cgi.FieldStorage()
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>%s</title>' % ('Library_type' )
print '</head>'
print '<body>'

print """<form action="/cgi-bin/xxxx.py" method="GET" target="_blank"><br>SAMPLE_TYPE:<select>
  <optgroup label="WGS">
    <option value="WGS_NEXTFLEX">NEXTFLEX</option>
  </optgroup>
  <optgroup label="TRUE_SEQ">
  <option value="TRUE_SEQ">TRUE_SEQ</option>
  </optgroup>
  <optgroup label="Tagmentation">
    <option value="SMALL_RNA">SMALL_RNA</option>
    <option value="SMALL_RNA_TOTAL_RNA">TOTAL_RNA</option>
  </optgroup>
</select><br>"""
list=['BA','QUBIT','qPCR']
print '<table>'
for i in list:
    print """<tr><td>%s: <select name= "option"><option value ="YES" > YES </option><option value ="NO" > NO </option></td><br>
""" % (i)
print '</table>'
print '</form>'
print '</body>'
print '</html>'


