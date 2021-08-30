#!/usr/bin/python
import cgi
import MySQLdb
import cgitb; cgitb.enable()
form = cgi.FieldStorage()

def htmlTop():
    print """Content-type: text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                 <head>
                     <title>{} {} {}</title>
                 </head>
                 <body>""".format(field_value,summ_value,field_filter)
def htmlTail():
    print """ </body>
        </html>""" 
def connectDB():
    db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
    db1= db.cursor()
    return db, db1
def selectPeople(db, db1):
    sql= "SELECT * FROM plan where {}= '{}';"
    db1.execute(sql.format(field_filter, field_value))
    rows= db1.fetchall()
    summ=0.0
    people=[]
    for row in rows:
        summ=summ+float(row[10])
        if summ<=summ_value:
            people.append(row)    
    return people

def xl(people):
    import xlwt
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('final_plan')
    header=['ID', 'SO_NUMBER', 'SAMPLE_ID', 'CLIENT', 'NO_OF_SAMPLE', 'ORGANISM', 'CHEMISTRY', 'APPLICATION', 'MIN_READS', 'MAX_READS', 'TO_RUN', 'AVG_SIZE', 'AVERAGE_NM', 'QUBIT_NG', 'BARCODE_NAME1', 'BARCODE_SEQ1', 'BARCODE_SEQ2', 'BARCODE_NAME2', 'MACHINE_TYPE']
    for index, value in enumerate(header):
        worksheet.write(0, index, value)
    
    for row_index, row_value in enumerate(people):
        for col_index, col_value in enumerate(row_value):
            worksheet.write(row_index+1, col_index, col_value)

    workbook.save('FINAL_PLAN.xls')    
    
    

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
    print "<th bgcolor=FF00CC>MACHINE_TYPE</th>"
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
        print "<td bgcolor=55ff55>{0} </td>".format(each[18])
        print "</tr>"
    print "</table>"

def button():
    print """<br><br>Download_Final_plan: <a href="//localhost/FINAL_PLAN.xls" class="button">
                   Dowload_xl!
                        </a>"""

def backup_Runnedplan(people):
    print """<form action="/cgi-bin/Manual_Runned_plan.py" method="POST">"""
    print "<br><br><table border= '1'>"
    print """<tr><td>BACKUP_RUNNED_PLAN:::</td><td><input type="hidden" name="FIELD" value='{}'>
<input type="hidden" name="SUM" value={}><td><input type="hidden" name="FIELD_VALUE" value='{}'></td><td><input type="submit" value="SUBMIT" /></td></tr></table></form>""".format(field_filter, summ_value, field_value)



if __name__ == "__main__":
    try:
        field_filter=(form["field"].value).upper()
        field_value=(form["field_value"].value).upper()
        summ_value=float(form["summ_value"].value)
        htmlTop()
        db, db1 =connectDB()
        people = selectPeople(db,db1)
        print "{}".format(people)
        db1.close()
        xl(people)
        displayPeople(people)
        button()
        backup_Runnedplan(people)
        htmlTail()
    except:
        print "Content-type:text/html\r\n\r\n"
        print '<html>'
        print '<body style="background-color:red;">'
        print "<hr><hr><hr><br>Please Enter all the fields area<br><br><hr><hr><hr>"
        print '</body>'
        print '</html>'

        

