#!/usr/bin/python
import cgi
import cgitb;cgitb.enable()
form = cgi.FieldStorage()
import MySQLdb
def htmlTop():
    print """Content-type: text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                 <head>
                     <title> tabale</title>
                 </head>
                 <body>"""
def htmlTail():
    print """ </body>
        </html>""" 

def connectDB():
    db=MySQLdb.connect("localhost", "root", "root", "REPORT_AUTOMATION")
    db1= db.cursor()
    return db, db1
def selectRecords(db, db1):
    sql= "SELECT * FROM REPORT;"
    db1.execute(sql)
    records= db1.fetchall()
    return records

def createDropDown(records):
    print """<select name="drop">"""
    for id in records:
        print"""<option value ="{0}" > {0} </option> """.format(id[0])
    print"""</select><br>"""
def createDropDownField(fields):
    print """<select name= "field">"""
    for entry in fields:
        print """<option value="{0}">{0} </option>""".format(entry)
    print """</select><br>"""

def createForm(records,fields):
    print """<form method="post" action= "Second_UpdateDatabase.py">""" 
    print"<table cellspacing ='5'>"
    print"""<tr>
              <td bgcolor=55ff55>UPDATE"""
    createDropDown(records)
    print"""</td >
              <td>"""
    createDropDownField(fields)
    print"""</td>
             <td>"""
    print """<input type="text" name="testing" value=''>"""
    print """</td>
             <td>"""
    print '<input type="submit" value="Submit" />' 
    print """</td>
             </tr>"""
    print "</table>"
    print "</form>"


def displayRecords(records):
    print "<table border= '1'>"
    print "<tr>"
    print "<th bgcolor=FF00CC>ID</th>"
    print "<th bgcolor=FF00CC>SO_NUMBER</th>"
    print "<th bgcolor=FF00CC>PROJECT_OBJECTIVE</th>"
    print "<th bgcolor=FF00CC>PROJECT_TYPE</th>"
    print "<th bgcolor=FF00CC>SAMPLE_TYPE</th>"
    print "<th bgcolor=FF00CC>GEL_REPORT</th>"
    print "<th bgcolor=FF00CC>BA_REPORT</th>"
    print "<th bgcolor=FF00CC>TABLE_REPORT</th>"
    print "<th bgcolor=FF00CC>MOL_RESULT</th>"

    for each in records:
        print "<tr>"
        print "<td bgcolor=55ff55>{0} </td>".format(each[0])
	print "<td bgcolor=55ff55>{0} </td>".format(each[1])
        shortlen=each[2][:25]
	print "<td bgcolor=55ff55>{0} </td>".format(shortlen)
	print "<td bgcolor=55ff55>{0} </td>".format(each[3])
        print "<td bgcolor=55ff55>{0} </td>".format(each[4])
        print "<td bgcolor=55ff55>{0} </td>".format(each[5])
        print "<td bgcolor=55ff55>{0} </td>".format(each[6])
        print "<td bgcolor=55ff55>{0} </td>".format(each[7])
        print "<td bgcolor=55ff55>{0} </td>".format(each[8])

        print "</tr>"
    print "</table>"


if __name__ == "__main__":
    try:
        htmlTop()
        db, db1 =connectDB()
        records = selectRecords(db,db1)
        db1.close()
        displayRecords(records)
        fields=['SO_NUMBER', 'PROJECT_OBJECTIVE', 'PROJECTIVE_TYPE']
        htmlTail()
    except:
        cgi.print_exception()   



