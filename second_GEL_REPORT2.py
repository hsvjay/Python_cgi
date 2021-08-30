#!/usr/bin/python
import cgi, os
import cgitb; cgitb.enable()
import MySQLdb
import urllib
form = cgi.FieldStorage()
SO_NUMBER=form['hidden'].value
fileitem = form['GEL_REPORT2']

print "Content-type:text/html\r\n\r\n"
print '<html>'
print "<body>"

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
sql1="SELECT GEL_REPORT2, SAMPLE_TYPE FROM REPORT WHERE SO_NUMBER='{}'".format(SO_NUMBER)
db1.execute(sql1)
path="""/var/www/SO_NUMBER/{}""".format(SO_NUMBER)
String_Value=db1.fetchall()
sample_type= urllib.pathname2url(String_Value[0][1])
SAMPLE_TYPE= String_Value[0][1]
if String_Value[0][0] !='YES':
    if not os.path.isdir('{}'.format(path)):
        os.mkdir(path)
        from shutil import copyfile
        copyfile(filepathname, "{}/{}".format(path, fn))
    else:
        from shutil import copyfile
        copyfile(filepathname, "{}/{}".format(path, fn))

    sql="UPDATE REPORT SET GEL_REPORT2 = 'YES' WHERE SO_NUMBER = '{}';".format(SO_NUMBER)
    db1.execute(sql)
    db.commit()
    print """THE REPORT NAMED {2} HAS BEEN SUCCESSFULLY PLACED FOR THE SO_NUMBER: {0}<meta http-equiv="refresh" content="7;url=http://localhost/cgi-bin/second_type2.py?SAMPLE_TYPE={0}&hidden={1}" />""".format(sample_type, SO_NUMBER, fn)    


else:
    print """THE Folder named {1} contains the file named {2} exists
    <meta http-equiv="refresh" content="7;url=http://localhost/cgi-bin/second_type2.py?SAMPLE_TYPE={0}&hidden={1}" />""".format(sample_type, SO_NUMBER, fn)

    print '</body>'
    print '</html>'
    
db.close()
print "{} SO_NUMBER: {}, '{}', {}<br>".format(String_Value[0][0], SO_NUMBER, fn , path)
print '</body>'
print '</html>'



