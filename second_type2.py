#!/usr/bin/python
import cgi
import cgitb;cgitb.enable()
import MySQLdb
form = cgi.FieldStorage()
db=MySQLdb.connect("localhost","root", "root", "REPORT_AUTOMATION")
db1=db.cursor()
sql= "SELECT *  FROM REPORT WHERE SO_NUMBER='{}';"
SO_NUMBER=(form['hidden'].value)
SAMPLE_TYPE=((form['SAMPLE_TYPE'].value).upper().rstrip())
db1.execute(sql.format(SO_NUMBER))
SO_LIST=db1.fetchall()

upd_sql= "UPDATE REPORT SET  SAMPLE_TYPE = '{}' WHERE SO_NUMBER='{}'".format(SAMPLE_TYPE, SO_NUMBER)
db1.execute(upd_sql)
db.commit()
itrn=0
if SAMPLE_TYPE == "DNA+RNA":
    itrn=1


print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<body>{},  SO_NUMBER: {} ,{}, {}<br><br>'.format('Molecular_biology', SO_NUMBER, SO_LIST, SAMPLE_TYPE)
if SO_LIST != ():
    for itr in range(0,itrn+1):
        if SO_LIST[0][5 + (itr*4)] == 'NA':   
            print """<form enctype="multipart/form-data" action="second_GEL_REPORT{0}.py" method="post">
                 <table><tr><td><br><h2 style="font-size:75%;">UPLOAD_GEL_REPORT{0}:<input type="file" name="GEL_REPORT{0}" /><h2></td><td><input type="hidden" name="hidden" value={1}></td>""".format(itr+1, SO_NUMBER)
            print '<td><input type="submit" value="Upload" /></td>'
            print '</tr></table></form>'
        else:
            print """<h2 style="font-size:75%;">GEL_REPORT_UPLOADED...<br><br></h2><br>"""
        if SO_LIST[0][6 + (itr*4)] == 'NA':
            print """<form enctype="multipart/form-data" action="second_BA_REPORT{0}.py" method="post">
                 <table><tr><td><br><h2 style="font-size:75%;">UPLOAD_BA_REPORT{0}:<input type="file" name="BA_REPORT{0}" /><h2></td><td><input type="hidden" name="hidden" value={1}></td>""".format(itr+1,SO_NUMBER)
            print '<td><input type="submit" value="Upload" /></td>'
            print '</tr></table></form>'
        else:
            print """<h2 style="font-size:75%;">BA_REPORT_UPLOADED...</h2><br><br>"""
        if SO_LIST[0][7 + (itr*4)] == 'NA':
            print """<form enctype="multipart/form-data" action="second_TABLE_REPORT{0}.py" method="post">
                 <table><tr><td><br><h2 style="font-size:75%;">UPLOAD_TABLE_REPORT{0}:<input type="file" name="TABLE_REPORT{0}" /><h2></td><td><input type="hidden" name="hidden" value={1}></td>""".format(itr+1,SO_NUMBER)
            print '<td><input type="submit" value="Upload" /></td>'
            print '</tr></table></form>'
        else:
            print """<h2 style="font-size:75%;">TABLE_REPORT_UPLOADED...</h2><br><br>"""
    
    if SO_LIST[0][8] == 'NA':
        print """<form action="/cgi-bin/second_result.py" method="post"><br> """
        print """<br><h2 style="font-size:75%;"> RESULT:</h2><br><textarea rows="6" cols="120" name="RESULT"></textarea><br><input type="hidden" name="hidden" value={}>""".format(SO_NUMBER)
        print """<input type="submit" style="background-color:FF6666;color:990000;border-radius:5px; border:2px solid #CC6699" value="submit"><br/>"""
        print """</form>"""
    else:
        print """<h2 style="font-size:75%;">RESULT ENTERED..</h2></h2>"""
    print '</body>'
    print '</html>'
else:
    print """<h2 style="font-size:75%;">The entered SO_NUMBER DOESN'T EXISTS IN THE DATABASE</h2><br>"""
    print '</body>'
    print '</html>'

