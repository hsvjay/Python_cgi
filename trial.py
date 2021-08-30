#!/usr/bin/python
import MySQLdb
import cgi
import cgitb; cgitb.enable()
form=cgi.FieldStorage()
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<body>hello!'
print '</body>'
print '</html'


