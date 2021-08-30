#!/usr/bin/python

import MySQLdb
import cgi
import cgitb;cgitb.enable()
form = cgi.FieldStorage()

print"""Content-type: text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                 <head><title>REGISTRATION</title>
                 </head>
                 <body>"""


try:
    SO_NUMB=(form['SO_NUMBER'].value).rstrip().upper()
    strr=(form['OBJECTIVE'].value).rstrip()
    Project_Type=form['project_type'].value
    db=MySQLdb.connect("localhost", "root", "root", "REPORT_AUTOMATION")
    db1= db.cursor()
    sql= "SELECT * FROM REPORT;"
    db1.execute(sql)
    if not SO_NUMB in [row[1] for row in db1.fetchall()]:
        db1.execute("""insert into REPORT( SO_NUMBER, PROJECT_OBJECTIVE, PROJECT_TYPE) values('{}','{}','{}')""".format(SO_NUMB,strr,Project_Type))
        db.commit()
        print 'updating<br>'
    print '{},{}'.format(SO_NUMB, Project_Type)
    print 'Wait, Redirecting_to_authorized_portal'
    print '<meta http-equiv="refresh" content="5;url=http://localhost/cgi-bin/second_login2.py?USER_ID={}&PASSWORD={}" />'.format('DUMMY', 'DUMMY')
    print '</body>'
    print '</html'

except KeyError:
    print "ONE OF THE FIELD AREA IS EMPTY! GO BACK AND RESUBMIT......"
    print '</body>'
    print '</html'

