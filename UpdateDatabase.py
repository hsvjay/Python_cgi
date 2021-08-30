#!/usr/bin/python
import cgi, os
import MySQLdb
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
def main():
    fileitem = int((form["drop"].value).upper())
    fileitem1=(form["field"].value).upper()
    fileitem2=(form["testing"].value).upper()
    fields=['SAMPLE_ID','CLIENT_NAME','ORGANISM','CHEMISTRY','APPLICATION','BARCODE_NAME1', 'BARCODE_SEQ1','BARCODE_SEQ2', 'BARCODE_NAME2' ]
    if not fileitem2 is '' and fileitem1 in fields:
        upd_sql= "UPDATE plan SET  {} = '{}' WHERE ID={}".format(fileitem1,fileitem2,fileitem)
        db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
        db1= db.cursor()
        db1.execute(upd_sql)
        db.commit()
        db.close()
        msg="Entered value loaded to the database"
    elif not fileitem2 is ' ':
        upd_sql= "UPDATE plan SET  {} = {} WHERE ID={}".format(fileitem1,fileitem2,fileitem)
        db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
        db1= db.cursor()
        db1.execute(upd_sql)
        db.commit()
        db.close()
        msg="fields loaded to the database"
    else:
        msg="invalid entry"
     
    print """Content-type:text/html\r\n\r\n
      <html>
      <body>  
      <p>fileitem</p>
      <p>%d,%s,%s, %s, %s</p>
      <meta http-equiv="refresh" content="5;url=http://localhost/Database.py" />
      </body>
      </html>""" % (fileitem,fileitem1,fileitem2,upd_sql, msg)

if __name__ == "__main__":
    try:
        main()
    except KeyError:
        print "Content-type:text/html\r\n\r\n"
        print '<html>'
        print '<body style="background-color:red;">'
        print "<hr><hr><hr><br>Please enter the value to update to the database<br><br><hr><hr><hr>"
        print '</body>'
        print '</html>'


   

