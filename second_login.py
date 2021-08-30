#!/usr/bin/python
keyword= "LOGIN PAGE"
def main():
    print "Content-type:text/html\r\n\r\n"
    print '<html>'
    print '<head>'
    print '<title>%s</title>' % ( keyword )
    print '</head>'
    print '<body style="background-color:black;">'
    print '<form action="/cgi-bin/second_login2.py" method="GET"><br />'
    print "<table align= 'center' cellspacing ='4'>"
    print"""<tr>
              <td >"""
    print"""<h2 style="color:blue;">LOGIN_USER_ID:</h2>
              </td>
              <td>
              <input type="text" style="background-color:00FFCC;color:blue;border:2px solid #9966FF;border-radius:5px"  name="USER_ID"><br />'
                 </td>
                <td>"""
    print"""<tr>
              <td>"""
    print"""<h2 style="color:Red;">PASSWORD:</h2>
              </td>
              <td>
             <input type="password" style="background-color:FF6666;color:990000;border-radius:5px; border:2px solid #CC6699" name="PASSWORD"><br/>'
               </td><td> <input type="submit" style="background-color:00FFCC;color:blue;border-radius:5px; border:2px solid #0000CC" value="submit">  <br />'
              </td>
              </tr>"""
    print "</table>"
    print '</form>'
    print '</body>'
    print '</html>'
main()

