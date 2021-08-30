#!/usr/bin/python
import cgi, os, sys
import cgitb; cgitb.enable()
import MySQLdb
form = cgi.FieldStorage()
SO_NUMBER=form['hidden'].value
fileitem = form['GEL_REPORT']

if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'


filepathname= '/tmp/'+ fn
db=MySQLdb.connect("localhost", "root","root","REPORT_AUTOMATION")
db1=db.cursor()
sql1="SELECT GEL_REPORT FROM REPORT WHERE SO_NUMBER='{}'".format(SO_NUMBER)
db1.execute(sql1)
path="""/home/vijay"""
String_Value=db1.fetchall()
if String_Value[0][0] !='YES':
    if not os.path.isdir('{}'.format(path)):
        os.chdirs(path,0755);
        from shutil import copyfile
        copyfile(filepathname, "/home/vijay/{}".format(SO_NUMBER, fn))
    sql="UPDATE REPORT SET GEL_REPORT = 'YES' WHERE SO_NUMBER = '{}';".format(SO_NUMBER)
    db1.execute(sql)
    db.commit()
db.close()
print "Content-type:text/html\r\n\r\n"
print '<html>'
print "<body>{}, SO_NUMBER: {}, '{}', {}<br>".format('Molecular_biology', SO_NUMBER, fn , path)
print '</body>'
print '</html>'



