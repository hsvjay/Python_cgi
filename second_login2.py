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
        print '<body>hello!<br>'
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

        print '<form action="/cgi-bin/second_New_Records_Mol.py" method="post">'
        print 'MOL_BIO_LAB:<input type="submit" value="REPORT_UPDATION_PENDING" />'
        print '</form>'

        print '<form action="/cgi-bin/" method="post">'
        print 'NGS_LAB:<input type="submit" value="REPORT_UPDATION_PENDING" />'
        print '</form>'
        
        print '</body>'
        print '</html>'
    elif (form['USER_ID'].value).upper() =="MOLBIO" and (form['PASSWORD'].value).upper() =="MOLBIO":
        print '<div align="center"><h1 style="color:brown;">MOLBIO_LAB_REPORT_SUBMISSION_PORTAL</h1></div>'
        print '<p align=center><img src="/cgi-bin/banner6.jpg" width=900 height=220 border=2 alt=""></p>'

        print '<form action="/cgi-bin/second_Old_Records_Mol.py" method="post">'
        print 'RECORDS_IN_DATABASE:<input type="submit" value="RECORDS_VIEW" />'
        print '</form>'

        print '<form action="/cgi-bin/second_New_Records_Mol.py" method="post">'
        print 'NEW_RECORDS_FOR_TESTING:<input type="submit" value="REPORT_UPDATION_PENDING" />'
        print '</form>'
      
        print '<form action="/cgi-bin/second_type2_Sample_type.py" method="GET">'
        print"<table align='left' cellspacing ='5'>"
        print"""<tr>
              <td>"""
        print"""<h2 style="color:Red;">ENTER_SO_NUMBER_TO_UPLOAD_REPORTS:</h2></td>
               <td> <input type="text" name="SO_NUMBER">
                <input type="submit" style="background-color:FF6666;color:990000;border-radius:5px; border:2px solid #CC6699" value="submit">
               </td><br />"""
        print "</table>"
        print '</form>'
       
        print '</body>'
        print '</html>'
    elif (form['USER_ID'].value).upper() =="NGS" and (form['PASSWORD'].value).upper() =="NGS":
        print '<div align="center"><h1 style="color:brown;">NGS_LAB_REPORT_SUBMISSION_PORTAL</h1></div>'
        print '<p align=center><img src="/cgi-bin/banner6.jpg" width=900 height=220 border=2 alt=""></p>'

        print '<form action="/cgi-bin/second_Old_Records_Mol.py" method="post">'
        print 'RECORDS_IN_DATABASE:<input type="submit" value="RECORDS_VIEW" />'
        print '</form>'

        print '<form action="/cgi-bin/second_New_Records_NGS.py" method="post">'
        print 'NEW_RECORDS_FOR_NGS_RUN:<input type="submit" value="REPORT_UPDATION_PENDING" />'
        print '</form>'
        list=['BA','QUBIT','qPCR']
        print """<form action="/cgi-bin/second_type3_NGS.py" method="post" target="_blank">
                <table align= 'left' cellspacing ='4'><tr>
                                         ########REPORT_UPDATION_ENTRY###########<br>
           <br> <td ><h3 style="color:blue;">ENTER_SO_NUMBER:</h2></td>
              <td><input type="text" style="background-color:00FFCC;color:blue;border:2px solid #9966FF;border-radius:5px"  name="SO_NUMBER"><br /></td></table>
                 <table  cellspacing ='4'><tr><td>
                      LiBRARY_TYPE:</td><td><select name="LIB_TYPE">
                     <optgroup label="WGS_NEXTFLEX">
                     <option value="WGS_NEXTFLEX">NEXTFLEX</option>
                     </optgroup>
                     <optgroup label="WGS_TRUE_SEQ">
                     <option value="WGS_TRUE_SEQ">TRUE_SEQ</option>
                     </optgroup>
                     <optgroup label="WGS_Tagmentation">
                     <option value="SMALL_RNA">SMALL_RNA</option>
                     <option value="SMALL_RNA_TOTAL_RNA">TOTAL_RNA</option>
                     </optgroup>
                     </optgroup>
                     </select></td><tr><td ><h4 style="color:blue;">a: DNA:</h4></td>
              <td><input type="text" style="background-color:00FFCC;color:blue;border:2px solid #9966FF;border-radius:5px"  name="DNA"></td></tr></tr><tr>
              <td ><h4 style="color:blue;">b: FRAGMENT_SIZE:</h4></td><td><input type="text" style="background-color:00FFCC;color:blue;border:2px solid #9966FF;border-radius:5px"  name="FRAGMENT_SIZE"></td></tr><tr>
              <td ><h4 style="color:blue;">c: BA:</h4></td><td><input type="text" style="background-color:00FFCC;color:blue;border:2px solid #9966FF;border-radius:5px"  name="BA_TXT"></td></tr><tr>
              <td ><h4 style="color:blue;">d: PCR_CYCLES:</h2></td><td><input type="text" style="background-color:00FFCC;color:blue;border:2px solid #9966FF;border-radius:5px"  name="PCR_CYCLES"></td></tr></table><br><br>"""
        print """<table align='left' cellspacing ='10'><tr>"""
        for i in list:
            print """<td>{0}: <select name={0}><option value ="YES" > YES </option><option value ="NO" > NO </option></td> """.format(i)
        print '</tr></table><br><br>'
    
        print """<br>REPORT: <br><textarea rows="6" cols="120" style="background-color:00FFCC;color:blue;border:2px solid #9966FF;border-radius:10px" name="REPORT"></textarea>"""

        
        print """<input type="submit" value="Submit" /></form>"""

        print '</body>'
        print '</html>'

        
    else:
        print "<br>The User_name and password entered is incorrect!"
        print '</body>'
        print '</html>'

try:
    main()
except KeyError:
    print "NOT ENTERED PASSWORD OR USER_NAME"
    print '</body>'
    print '</html>'

