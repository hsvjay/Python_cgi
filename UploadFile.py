#!/usr/bin/python
import MySQLdb
import cgi
import cgitb;cgitb.enable()
form = cgi.FieldStorage()

def htmlTop():
    fileitem = form['SO_NUMBER'].value.upper()
    print("""Content-type: text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                 <head><title>{}</title>
                 </head>
                 <body style="background-color:coral;">""").format(fileitem)
    return fileitem
def htmlTail():
    print (""" </body>
        </html>""")
def connectDB():
    db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
    db1= db.cursor()
    return db, db1
def selectPeople(db, db1, fileitem):
    sql= "SELECT SO_NUMBER, SAMPLE_ID, AVG_SIZE, QUBIT_NG,BARCODE_NAME1,BARCODE_SEQ1 FROM plan;"
    so_list=''
    db1.execute(sql)
    for row in db1.fetchall():
        if fileitem.rstrip() in row[0]:
            so_list=row
            break
    return so_list
def fileupload(fileitem, so_list):
    if fileitem.rstrip() in so_list:
        print '<h1 style="font-family:verdana;">Record for {} exist!</h1>'.format(so_list)
        x=2
        if(x is 2):
            print '<form enctype="multipart/form-data" action="save_file.py" method="post">'
                  
            print '<br>PRS: <input type="file" name="PRS"> </h2>'
            print '<input type="hidden" name="hidden" value={}>'.format(fileitem)
            print '<input type="submit" value="Upload" />'
            print '</form>'
        else:
            print'<br><h2 style="font-size:100%;">PRS report uploaded</h2>'
        if('NA' in so_list[1]):
            print '<form enctype="multipart/form-data" action="qc_save_file.py" method="post">'
            print '<br>QC_FILE: <input type="file" name="QC" />'
            print '<input type="hidden" name="hidden" value={}>'.format(fileitem)
            print '<input type="submit" value="Upload" />'
	    print '</form>'
        else:
            print '<br><h2 style="font-size:100%;">QC report uploaded<br/></h2>'

	if(so_list[2]==0.0):
            print '<form enctype="multipart/form-data" action="qPCR_save_file.py" method="post">'
            print '<br>qPCR: <input type="file" name="qPCR" />'
            print '<input type="hidden" name="hidden" value={}>'.format(fileitem)
            print '<input type="submit" value="Upload" />'
            print '</form>'
        else:
            print '<br><h2 style="font-size:100%;">qPCR report uploaded</h2>'

        if('NA' in so_list[4]):
            print '<form enctype="multipart/form-data" action="LIB_save_file.py" method="post">'
            print '<table><tr><td><br><h2 style="font-size:65%;">BARCODE_SEQUENCE_AND_NAME_NOT_UPLOADED.DO_U_LIKE_TO_UPLOAD_LIBRARY_PREP_KIT?<h2></td><td>: <input type="file" name="LIB" /></td>'
            print '<input type="hidden" name="hidden" value={}>'.format(fileitem)
            print '<td><input type="submit" value="Upload" /></td>'
            print '</tr></table></form>'
        else:
            print '<form enctype="multipart/form-data" action="BarcodeCheck.py" method="post">'
            print '<table><tr><td><br><h2 style="font-size:65%;">BARCODE_NAME_AND_SEQ_UPLOADED.Verify_BARCODES_BY_UPLOADING_KIT_REPORT:<h2></td><td> <input type="file" name="LIB" /></td>'
            print '<input type="hidden" name="hidden" value={}>'.format(fileitem)
            print '<td><input type="submit" value="Upload" /></td>'
            print '</tr></table></form>'
            """
            print '<form enctype="multipart/form-data" action="VerifyingBarcodes.py" method="post">'
            print '<table><tr><td><br><h2 style="font-size:75%;">BARCODE_NAME_AND_SEQ_UPLOADED.Verify_BARCODES_BY_UPLOADING_KIT_REPORT: <input type="file" name="LIB" /><h2></td>'
            print '<input type="hidden" name="hidden" value={}>'.format(fileitem)
            print '<td><input type="submit" value="Upload" /></td>'
            print '</tr></table></form>"""
        print '<form action="/cgi-bin/Database.py" method="POST">'
        print ' <br><input type="submit" value="TABLE_VIEW">  <br />'
        print '</form>'
    else:
        print 'Queried SO_NUMBER doesn\'t exist'
   

if __name__ == "__main__":
    try:
        fileitem=htmlTop()
        db, db1 =connectDB()
        so_list= selectPeople(db,db1, fileitem)
        db1.close()
        fileupload(fileitem,so_list)
        htmlTail()
    except:
        print """Content-type: text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                 <body style="background-color:red;">"""
        print "<hr><hr><hr><br><h1>PLEASE PLUG IN THE SO_NUMBER<h1><br><hr><hr><hr>"
        htmlTail()
