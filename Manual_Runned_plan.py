#!/usr/bin/python
import cgi
import MySQLdb
import cgitb; cgitb.enable()
form = cgi.FieldStorage()

FIELD=form['FIELD'].value
SUM=float(form['SUM'].value)
FIELD_VALUE= form['FIELD_VALUE'].value

def htmlTop():
    print """Content-type: text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                 <head>
                     <title>Back_up</title>
                 </head>
                 <body>{},{},{}""".format(FIELD,FIELD_VALUE,SUM)


def connectDB():
    db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
    db1= db.cursor()
    return db, db1

def selectPeople(db, db1):
    sql= "SELECT * FROM plan where {}= '{}';"
    db1.execute(sql.format(FIELD, FIELD_VALUE))
    rows= db1.fetchall()
    summ=0.0
    people=[]
    for row in rows:
        summ=summ+float(row[10])
        if summ<=SUM:
            people.append(row)
    return people


def connectDBR(people):
    dbR=MySQLdb.connect("localhost", "root", "root", "Runned_plan")
    dbR1= dbR.cursor()
    sql1= """insert into plan(ID, SO_NUMBER, SAMPLE_ID, CLIENT_NAME, NO_OF_SAMPLE, ORGANISM, CHEMISTRY, APPLICATION, MIN_READS, MAX_READS, TO_RUN, AVG_SIZE, AVERAGE_NM, QUBIT_NG, BARCODE_NAME1, BARCODE_SEQ1, BARCODE_SEQ2, BARCODE_NAME2, Machine_Type) VALUES( {},'{}','{}','{}',{},'{}','{}','{}',{},{},{},{},{},{},'{}','{}','{}','{}','{}')"""
    for i in people:
        dbR1.execute(sql1.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18]))
    dbR.commit()
    dbR.close()
    print "<hr>The database Runned_plan is backed_up<hr>"

def Delete_Rows(people):
    IDS= zip(*people)[0]
    sql = "DELETE FROM plan WHERE ID={}"
    db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
    db1= db.cursor()
    for i in IDS:
        db1.execute(sql.format(i))
    db.commit()
    db.close()


def htmlTail():
    print """ </body>
        </html>"""


if __name__ == "__main__":
    try:
        FIELD=form['FIELD'].value
        SUM=float(form['SUM'].value)
        FIELD_VALUE= form['FIELD_VALUE'].value
        htmlTop()
        db, db1 = connectDB()
        people = selectPeople(db,db1)
        print "{}".format(people)
        db.close()
        connectDBR(people)
        Delete_Rows(people)
        htmlTail()
    except:
        print '<html>'
        print '<body style="background-color:red;">'
        print "<hr><hr><hr><br>Records are already stored in the database<br><br><hr><hr><hr>"
        print '</body>'
        print '</html>'






