#!/usr/bin/python
import cgi, os
import cgitb; cgitb.enable()
import MySQLdb
form = cgi.FieldStorage()
SO_NUMBER=form['hidden'].value

db=MySQLdb.connect("localhost", "root","root","REPORT_AUTOMATION")
db1=db.cursor()
sql1="SELECT BA_REPORT FROM REPORT WHERE SO_NUMBER='{}'".format(SO_NUMBER)
db1.execute(sql1)
String_Value=db1.fetchall()
if String_Value[0][0] !='YES':
    sql="UPDATE REPORT SET BA_REPORT = 'YES' WHERE SO_NUMBER = '{}';".format(SO_NUMBER)
    db1.execute(sql)
    db.commit()
db.close()
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<body>{}, SO_NUMBER: {}<br>'.format('Molecular_biology', SO_NUMBER)
print '</body>'
print '</html>'
