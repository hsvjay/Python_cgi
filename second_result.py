#!/usr/bin/python
import MySQLdb
import cgi
import cgitb;cgitb.enable()
form = cgi.FieldStorage()

RESULT=(form['RESULT'].value).upper()
SO_NUMBER=form['hidden'].value

db=MySQLdb.connect("localhost", "root","root","REPORT_AUTOMATION")
db1=db.cursor()
sql="UPDATE REPORT SET MOL_RESULT = '{}'  WHERE SO_NUMBER = '{}';".format(RESULT, SO_NUMBER)
db1.execute(sql)
db.commit()
db.close()

print "Content-type:text/html\r\n\r\n"
print '<html>'
print "<body>'{}'  SO_NUMBER: '{}'<br>".format(RESULT, SO_NUMBER)

print '</body>'
print '</html>'


