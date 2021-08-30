#!/usr/bin/python

import cgi, os
import MySQLdb
import csv
import cgitb; cgitb.enable()

form = cgi.FieldStorage()
# Get filename here.
hid=form['hidden'].value
fileitem = form['qPCR']

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
 
filepathname='/tmp/' +fn

filepathname= '/tmp/'+ fn
'''row_list=[]
with open(filepathname,'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(spamreader):
        if (i>14) and (i<15+int(iterrn)):
            row_list.append(row)
    sample_id_list=zip(*row_list)[1] 

'''
Average_size=[]
Average_nm=[]
Qubit_nm=[]

with open(filepathname,'rb') as csvfile:
    reader=csv.reader(csvfile, delimiter = ',')
    for i in reader:
        if '{}'.format(hid) in (i[0]).upper():
            Average_size.append(float(i[8]))
            Average_nm.append(float(i[19]))
            Qubit_nm.append(float(i[21]))
if len(id_nos) is len(Average_size):
    db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
    db1= db.cursor()

    upd_sql= "UPDATE plan SET AVG_SIZE = {}, AVERAGE_NM ={},QUBIT_NG = {} WHERE id={}"
    for j,k in enumerate(id_nos):
        db1.execute(upd_sql.format(Average_size[j], Average_nm[j], Qubit_nm[j], k ))
    db.commit()
    db.close()
print """\
Content-Type: text/html\n
<html>
<body>	
   <p>fileitem</p>
   <p>%s, %s, %s</p>
</body>
</html>
""" % (Average_size, Average_nm, Qubit_nm, )
print """\
<html> 
  <head> 
    <meta http-equiv="refresh" content="7;url=http://localhost/UploadFile.py?SO_NUMBER={}" /> 
    <title>You are going to be redirected</title> 
  </head> 
  <body> 
    Redirecting...
  </body> 
</html> """.format(hid)
