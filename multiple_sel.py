#!/usr/bin/python
import cgi
import cgitb;cgitb.enable()
print 'Content-type: text/html\r\n\r'
print """<!DOCTYPE html>
<html>
<body style="background-color:thistle;">

<form action="example.py">
<select name="cars" multiple>
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="opel">Opel</option>
  <option value="audi">Audi</option>
</select>
<input type="submit">
</form>"""
print '</body>'
print '</html>'

