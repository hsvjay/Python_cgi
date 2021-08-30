#!/usr/bin/python
import cgi
import cgitb;cgitb.enable()
import MySQLdb
form = cgi.FieldStorage()
SO_NUMBER=(form['SO_NUMBER'].value).upper().rstrip()
db=MySQLdb.connect("localhost","root", "root", "REPORT_AUTOMATION")
db1=db.cursor()
sql= "SELECT SO_NUMBER FROM REPORT WHERE SO_NUMBER='{}' ;"
db1.execute(sql.format(SO_NUMBER))
SO_LIST=db1.fetchall()

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<body>{},  SO_NUMBER: {}<br>'.format('Molecular_biology', SO_NUMBER)
if SO_LIST != ():
    db1.execute("SELECT SAMPLE_TYPE FROM REPORT WHERE SO_NUMBER='{}';".format(SO_NUMBER))
    SAMPLE_TYPE = db1.fetchone()
    if SAMPLE_TYPE[0] == 'NA':
        print """<form action="/cgi-bin/second_type2.py" method="GET">
  <br><table cellspacing ='5'><tr><td><h2 style="font-size:75%;">SAMPLE_TYPE:</h2></td><td><select name='SAMPLE_TYPE'>
  <optgroup label="DNA">
    <option value="DNA_WGS">DNA_WGS</option>
    <option value="DNA_AMPLICON">AMPLICON</option>
  </optgroup>
  <optgroup label="RNA">
  <option value="TOTAL_RNA">TOTAL_RNA</option>
  </optgroup>
  <optgroup label="SMALL_RNA">
    <option value="SMALL_RNA">SMALL_RNA</option>
    <option value="SMALL_RNA_TOTAL_RNA">TOTAL_RNA</option>
  </optgroup>
  <optgroup label="DNA+RNA">
  <option value="DNA+RNA">DNA+RNA</option>
  </optgroup>
</select></td><input type="hidden" name="hidden" value={}><td><input type="submit" style="background-color:FF6666;color:990000;border-radius:5px; border:2px solid #CC6699" value="submit"></td></table><br>
 """.format(SO_NUMBER) 
        print '{}</body>'.format(SAMPLE_TYPE[0])
        print '</html>'

    else:
        print """SAMPLE_TYPE_UPDATED_FOR_THIS_SO_NUMBER_PREVIOUSLY. HENCE,WAIT...., AS U R REDIRECTED TO REPORT UPLOAD PORTAL<meta http-equiv="refresh" content="4;url=http://localhost/cgi-bin/second_type2.py?SAMPLE_TYPE={0}&hidden={1}" />""".format(SAMPLE_TYPE[0], SO_NUMBER)
        print '</body>'
        print '</html>'

else:
    print "The ENTERED SO_NUMBER DOESN'T EXISTS"
    print '</body>'
    print '</html>'
    
