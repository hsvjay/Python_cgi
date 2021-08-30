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
    sql= "SELECT * FROM REPORT WHERE (GEL_REPORT= 'NA' OR BA_REPORT = 'NA' OR TABLE_REPORT='NA' OR MOL_RESULT= 'NA') OR ((GEL_REPORT2='NA' OR BA_REPORT2='NA' OR TABLE_REPORT2='NA') AND SAMPLE_TYPE='DNA+RNA');"
    db1.execute(sql)
    records= db1.fetchall()
    return records

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
        htmlTail()
    except:
        cgi.print_exception()




