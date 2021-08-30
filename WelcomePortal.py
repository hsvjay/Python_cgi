#!/usr/bin/python
keyword= "Welcome_to_NGS_RUNTIME_AUTOMATION"
def main():
    print "Content-type:text/html\r\n\r\n"
    print '<html>'
    print '<head>'
    print '<title>%s</title>' % ( keyword )
    print '</head>'
    print '<body style="background-color:black;">'
    print '<div align="center"><h1 style="color:brown;">Welcome_to_NGS_RUNTIME_PORTAL</h1></div>'
    print '<p align=center><img src="/cgi-bin/banner6.jpg" width=900 height=220 border=2 alt=""></p>'
    print '<form action="/cgi-bin/UploadFile.py" method="GET"><br />'
    print "<table align= 'center' cellspacing ='4'>"
    print"""<tr>
              <td >"""
    print"""<h2 style="color:blue;">LOGIN_SO_NUMBER:</h2>
              </td>
              <td>
                  <input type="text" style="background-color:00FFCC;color:blue;border:2px solid #9966FF;border-radius:5px"  name="SO_NUMBER"><br />'
                 </td>
                <td>
    <input type="submit" style="background-color:00FFCC;color:blue;border-radius:5px; border:2px solid #0000CC" value="submit">  <br />'
              </td>
              </tr>"""
    print "</table>" 
    print '</form>'
    print '<form action="/cgi-bin/Registrationform.py" method="GET">'
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
    print '</body>'
    print '</html>'
main()

