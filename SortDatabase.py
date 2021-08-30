#!/usr/bin/python
import cgi
import MySQLdb
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
sort_fd=(form["field"].value).upper()
order=(form["option"].value).upper()
def htmlTop():
    print """Content-type: text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                 <head>
                     <title>{}</title>
                 </head>
                 <body>""".format(sort_fd)
def htmlTail():
    print """ </body>
        </html>""" 
def connectDB():
    db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
    db1= db.cursor()
    return db, db1
def selectPeople(db, db1):
    sql= "SELECT * FROM plan ORDER BY {} {};"
    db1.execute(sql.format(sort_fd, order))
    people= db1.fetchall()
    return people
def createDropDown(people):
    print """<select name="drop">"""
    for id in people:
        print"""<option value ="{0}" > {0} </option> """.format(id[0])
    print"""</select><br>"""
def createDropDownField(fields):
    print """<select name= "field">"""
    for entry in fields:
        print """<option value="{0}">{0} </option>""".format(entry)
    print """</select><br>"""

def createDropDownMachine_Type(Machine_type):
    print """<form method="post" action= "machine_type.cgi">"""
    print"<table cellspacing ='5'>"
    print"""<tr>
              <td bgcolor=55ff55>"""
    print"""Machine_type:
              </td>
              <td bgcolor=55ff55>"""
    print """<select name="Machine_type">"""
    for id in Machine_type:
        print"""<option value ="{0}" > {0} </option> """.format(id[0])
    print"""</select><br>"""
    print """</td>
             <td>"""
    print '<input type="submit" value="Submit" />'
    print """</td>
             </tr>"""
    print "</table>"
    print "</form>"

def createForm(people,fields):
    print """<form method="post" action= "UpdateDatabase.py">""" 
    print"<table cellspacing ='5'>"
    print"""<tr>
              <td bgcolor=55ff55>"""
    createDropDown(people)
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
    
def displayPeople(people):
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
    for each in people:
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
        print "<td bgcolor=55ff55>{0} </td>".format(each[14])
        print "<td bgcolor=55ff55>{0} </td>".format(each[15])
        print "<td bgcolor=55ff55>{0} </td>".format(each[16])
        print "<td bgcolor=55ff55>{0} </td>".format(each[17])
        print "</tr>"
    print "</table>"


if __name__ == "__main__":
    try:
        htmlTop()
        db, db1 =connectDB()
        people = selectPeople(db,db1)
        db1.close()
        displayPeople(people)
        fields=['SAMPLE_ID','CLIENT_NAME','NO_OF_SAMPLE','ORGANISM','CHEMISTRY','APPLICATION', 'MIN_READS','MAX_READS','TO_RUN', 'AVG_SIZE', 'AVERAGE_NM','QUBIT_NG','BARCODE_NAME1', 'BARCODE_SEQ1','BARCODE_SEQ2', 'BARCODE_NAME2' ]
        Machine_type=['a','b','c','d','f','g','h']
        createForm(people,fields)
        createDropDownMachine_Type(Machine_type)
        htmlTail()
    except:
        cgi.print_exception()   

