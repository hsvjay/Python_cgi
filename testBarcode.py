#!/usr/bin/python
import MySQLdb
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
x=form["BARCODE_NAME11"].value


print """Content-type: text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                 <head><title></title>
                 </head>
                 <body>hello,{},{}""".format(form, x)
print "</body>"
print "</html>"
