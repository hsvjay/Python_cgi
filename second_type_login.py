#!/usr/bin/python
import cgi
import cgitb;cgitb.enable()
form = cgi.FieldStorage()
keyword= "Welcome_to_Report_AUTOMATION"
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>%s</title>' % ( keyword )
print '</head>'
print '<body style="background-color:orange;">'
def main():
    if (form['USER_ID'].value).upper() =="DUMMY" and (form['PASSWORD'].value).upper() =="DUMMY":
        print '<body>hello!<br>{} {}'.format(form['USER_ID'].value, form['PASSWORD'].value)
        print '<div align="center"><h1 style="color:brown;">AUTHORIZED_PERSON_PORTAL</h1></div>'
        print '<p align=center><img src="/cgi-bin/banner6.jpg" width=900 height=220 border=2 alt=""></p>'

        print '<form action="/cgi-bin/second_type1.py" method="GET">'
        print"<table align='center' cellspacing ='5'>"
        print"""<tr>
              <td>"""
        print"""<h2 style="color:Red;">REGISTER_SO_NUMBER:</h2>
              </td>
              <td>
    <input type="submit" style="background-color:FF6666;color:990000;border-radius:5px; border:2px solid #CC6699" value="New registr..."><br/>'
               </td>"""
        print "</table>"
        print '</form>'
        print '<form action="/cgi-bin/Second_Database.py" method="post">'
        print 'RECORDS_IN_DATABASE:<input type="submit" value="RECORDS_VIEW" />'
        print '</form>'

        print '<form action="/cgi-bin/MOLBIO_PENDING.py" method="post">'
        print 'MOL_BIO_LAB:<input type="submit" value="REPORT_UPDATION_PENDING" />'
        print '</form>'
      
        print '<form action="/cgi-bin/NGS_PENDING.py" method="post">'
        print 'NGS_LAB:<input type="submit" value="REPORT_UPDATION_PENDING" />'
        print '</form>'


        print '</body>'
        print '</html>'
    elif (form['USER_ID'].value).upper() =="MOLBIO" and (form['PASSWORD'].value).upper() =="MOLBIO":
        print '<body>hello!<br>{} {}'.format(form['USER_ID'].value, form['PASSWORD'].value)
        print '<div align="center"><h1 style="color:brown;">MOLBIO_LAB_REPORT_SUBMISSION_PORTAL</h1></div>'
        print '<p align=center><img src="/cgi-bin/banner6.jpg" width=900 height=220 border=2 alt=""></p>'
        








        print '<form action="/cgi-bin/second_New_Records_Mol.py" method="post">'
        print 'NEW_RECORDS_FOR_ANALYSIS:<input type="submit" value="NEW_RECORDS_VIEW" />'
        print '</form><br>'
        print """<form action="/cgi-bin/second_type2.py" method="post">"""
        print """ENTER_SO_#_TO_SUBMIT_REPORT:<input type="text" name="SO_NUMBER"><input type="submit" value="submit" /><br>"""
        print '</body>'
        print '</html>'
    else:
        print "<br>The User_name and password entered is incorrect!"
        print '</body>'
        print '</html>'

main()

