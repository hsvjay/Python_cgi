#!/usr/bin/python
import MySQLdb
import cgi, os
import cgitb;cgitb.enable()
form = cgi.FieldStorage()
def main():
    lis= form.getlist('Delete_Rows')
    if not len(lis) == 0:
        sql = "DELETE FROM plan WHERE ID={}"
        db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
        db1= db.cursor()
        for i in lis:
            db1.execute(sql.format(int(i)))
        db.commit()
        db.close()
        print "Content-Type:text/html\n\n"
        print "<html><body>"
        print "<hr><hr><hr><br><br>THE FOLLOWING IDS in the LIST: {} SELECTED FOR DELETION, HAS BEEN DELETED FROM THE Tentative_plan TABLE".format(lis)

        print '<br><form action="/cgi-bin/Database.py" method="POST">'
        print ' <br><hr><br>CLICK_TO_GET_BACK_TENTATIVE_PLAN_TABLE:<input type="submit" value="CLICK"><br><br><hr><hr><hr><br />'
        print '</form>'

        print "</body>"
        print "</html>"
    else:
        print """Content-type: text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                 <body style="background-color:red;">"""
        print "<hr><hr><hr><br><h1>PLEASE SELECT THE ROWS TO DELETE<h1><br><hr><hr><hr></body></html>"
      
        

if __name__ == "__main__":
    try:
        main()
    except KeyError:
        print """Content-type: text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                 <body style="background-color:red;">"""
        print "<hr><hr><hr><br><h1>PLEASE SELECT THE ROWS TO DELETE<h1><br><hr><hr><hr></body></html>"

