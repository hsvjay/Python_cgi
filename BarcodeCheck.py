#!/usr/bin/python
import MySQLdb
import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()
# Get filename here.
hid=form['hidden'].value
fileitem = form['LIB']

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'

db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
db1= db.cursor()
sql= "select ID, BARCODE_NAME1, BARCODE_SEQ1,BARCODE_NAME2, BARCODE_SEQ2 from plan where SO_NUMBER ='{}';".format(hid)
db1.execute(sql)
LIST = db1.fetchall()
db1.execute("SELECT * FROM plan;")
Records=db1.fetchall()
db.close()
SORT_LIST=sorted(LIST, key=lambda x: x[0])

filepathname= '/tmp/'+ fn
wdrecords=[]

from docx import Document
wordDoc = Document(filepathname)
for table in wordDoc.tables:
    for row in table.rows:
        for cell in row.cells:
            wdrecords.append((cell.text).encode("utf-8"))

barcodename1=[]
indexseq1=[]
for i in range(1,len(wdrecords)/7):
    barcodename1.append(wdrecords[5+7*i])
    indexseq1.append(wdrecords[6+7*i])


Nomatchb1_rowlist=[]
Nomatchs1_rowlist=[]
if len(SORT_LIST) is len(barcodename1):
    for i,j in enumerate(SORT_LIST):
        if(j[1] !='NA' and j[1] != barcodename1[i]):
            Nomatchb1_rowlist.append(j[0])
        if(j[2] !='NA' and j[2] != indexseq1[i]):
            Nomatchs1_rowlist.append(j[0])


print """\
Content-Type: text/html\n
<html> 
  <head>  
    <title>Verifying_BARCODES</title> 
  </head> 
  <body> 
    <h1 style="color:blue;">CHECKED_BARCODE_MATCHING</h2>
    Redirecting_{0}""".format(SORT_LIST)

print "<table border= '1'>"
print "<tr>"
print "<th bgcolor=FF00CC>ID</th>"
print "<th bgcolor=FF00CC>SO_NUMBER</th>"
print "<th bgcolor=FF00CC>SAMPLE_ID</th>"
print "<th bgcolor=FF00CC>CLIENT_NAME</th>"
print "<th bgcolor=FF00CC>NO_OF_SAMPLE</th>"
print "<th bgcolor=FF00CC>ORGANISM</th>"
print "<th bgcolor=FF00CC>CHEMISTRY</th>"
print "<th bgcolor=FF00CC>APPLICATION</th>"
print "<th bgcolor=FF00CC>MIN_READS</th>"
print "<th bgcolor=FF00CC>MAX_READS</th>"
print "<th bgcolor=FF00CC>TO_RUN</th>"
print "<th bgcolor=FF00CC>AVG_SIZE</th>"
print "<th bgcolor=FF00CC>AVERAGE_NM</th>"
print "<th bgcolor=FF00CC>QUBIT_NG</th>"
print "<th bgcolor=FF00CC>BARCODE_NAME1</th>"
print "<th bgcolor=FF00CC>BARCODE_SEQ1</th>"
print "<th bgcolor=FF00CC>BARCODE_SEQ2</th>"
print "<th bgcolor=FF00CC>BARCODE_NAME2</th>"
print "</tr>"
for each in Records:
    print "<tr>"
    print "<td bgcolor=55ff55>{0} </td>".format(each[0])
    print "<td bgcolor=55ff55>{0} </td>".format(each[1])
    print "<td bgcolor=55ff55>{0} </td>".format(each[2])
    print "<td bgcolor=55ff55>{0} </td>".format(each[3])
    print "<td bgcolor=55ff55>{0} </td>".format(each[4])
    print "<td bgcolor=55ff55>{0} </td>".format(each[5])
    print "<td bgcolor=55ff55>{0} </td>".format(each[6])
    print "<td bgcolor=55ff55>{0} </td>".format(each[7])
    print "<td bgcolor=55ff55>{0} </td>".format(each[8])
    print "<td bgcolor=55ff55>{0} </td>".format(each[9])
    print "<td bgcolor=55ff55>{0} </td>".format(each[10])
    print "<td bgcolor=55ff55>{0} </td>".format(each[11])
    print "<td bgcolor=55ff55>{0} </td>".format(each[12])
    print "<td bgcolor=55ff55>{0} </td>".format(each[13])
    if each[0] in Nomatchb1_rowlist:
        print "<td bgcolor=FF0000>{0} </td>".format(each[14])
    else:
        print "<td bgcolor=00FF00>{0} </td>".format(each[14])
    if each[0] in Nomatchs1_rowlist:
        print "<td bgcolor=FF0000>{0} </td>".format(each[15])
    else:
        print "<td bgcolor=00FF00>{0} </td>".format(each[15])
    print "<td bgcolor=55ff55>{0} </td>".format(each[16])
    print "<td bgcolor=55ff55>{0} </td>".format(each[17])
    print "</tr>"
print "</table>"

print '<form action="/cgi-bin/Database.py" method="post">'
print '<input type="submit" value="DATABASE_VIEW" />'
print '</form>'
print '</body>'
print '</html>'

