#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()
import MySQLdb
import csv
form = cgi.FieldStorage()
# Get filename here.

hid=form['hidden'].value
fileitem = form['QC']

db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
db1= db.cursor()
sql= "select ID, NO_OF_SAMPLE from plan where SO_NUMBER ='{}';".format(hid)
db1.execute(sql)
iterr=db1.fetchall()
db.close()
ID_SAMPLE_NO=zip(*iterr)
iterrn=ID_SAMPLE_NO[1][0]
id_nos=sorted(ID_SAMPLE_NO[0])

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('/tmp/' + fn, 'wb').write(fileitem.file.read())

    message = 'The file "' + fn + '" was uploaded successfully'
   
else:
    message = 'No file was uploaded'

filepathname= '/tmp/'+ fn
row_list=[]
with open(filepathname,'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(spamreader):
        if (i>14) and (i<15+int(iterrn)):
            row_list.append(row)
    sample_id_list=zip(*row_list)[1]


db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
db1= db.cursor()
'''setup if condition to check records'''
upd_sql="UPDATE plan SET SAMPLE_ID = '{}' WHERE id = {} "
for j,k in enumerate(id_nos):
    db1.execute(upd_sql.format(sample_id_list[j],k))
db.commit()
db.close()    
    

                  
print """\
Content-Type: text/html\n
<html>
<body>	
   <p>fileitem</p>
   <p>%s</p>
</body>
</html>
""" % (id_nos,)
print """\
<html> 
  <head> 
    <meta http-equiv="refresh" content="5;url=http://localhost/UploadFile.py?SO_NUMBER={}" /> 
    <title>You are going to be redirected</title> 
  </head> 
  <body> 
    Redirecting...'{}'
  </body> 
</html> """.format(hid,filepathname)
   
