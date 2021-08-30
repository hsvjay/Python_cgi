#!/usr/bin/python
import MySQLdb
import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()
# Get filename here.
hid=form['hidden'].value
fileitem = form['LIB']
 
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
wdrecords=[]
from docx import Document
wordDoc = Document(filepathname)
for table in wordDoc.tables:
    for row in table.rows:
        for cell in row.cells:
            wdrecords.append((cell.text).encode("utf-8"))
sample_name=[]
qubit_list=[]
nmpcr=[]
barcode=[]
indexseq=[]
for i in range(1,len(wdrecords)/7):
    sample_name.append(wdrecords[7*i])
    qubit_list.append(wdrecords[1+7*i])
    nmpcr.append(wdrecords[4+7*i])
    barcode.append(wdrecords[5+7*i])
    indexseq.append(wdrecords[6+7*i])

if len(id_nos) is len(sample_name):
    db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
    db1= db.cursor()
    upd_sql= "UPDATE plan SET BARCODE_NAME1= '{}', BARCODE_SEQ1= '{}' WHERE id={}" 
    for j,k in enumerate(id_nos):
        db1.execute(upd_sql.format(barcode[j],indexseq[j], k ))
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
""" % (wdrecords,)
print """\
<html> 
  <head> 
    <meta http-equiv="refresh" content="5;url=http://localhost/UploadFile.py?SO_NUMBER={}" /> 
    <title>You are going to be redirected</title> 
  </head> 
  <body> 
    Redirecting...
  </body> 
</html> """.format(hid)
