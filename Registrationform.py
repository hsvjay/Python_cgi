#!/usr/bin/python
import cgi
import cgitb;cgitb.enable()

print 'Content-type: text/html\r\n\r'
print '<html>'
def main():
    print '<hr><h1 align= left style="color:black;">Please enter the required fields</h1><hr>'
    print '<body style="background-color:thistle;">'
    print '<form action="/cgi-bin/BarcodeDefine.py" method="post">'

    print """<br><br><table align= center cellspacing ='10' border = '3'><tr><th bgcolor="FF99CC" style="color:990000;">SO_NUMBER :</th><th><input type="text" style="background-color:FF99CC;color:blue;border:2px solid #990000;border-radius:3px" name="SO_NUMBER"></th></tr>"""

    print """<tr><th bgcolor="FFCCF" style="color:CC3333;">CLIENT_NAME :</th><th><input type="text" style="background-color:FFCCFF;color:blue;border:2px solid #CC3333;border-radius:3px" name="CLIENT_NAME"></th></tr>"""

    print """<tr><th bgcolor="FF99CC" style="color:990000;">NUMBER_OF_SAMPLES :</th> <th> <input type="text" style="background-color:FF99CC;color:blue;border:2px solid #990000;border-radius:3px" name="SAMPLE_NUMBERS"></th><tr>"""
    print """<tr><th bgcolor="FFCCFF" style="color:CC3333;">TO_RUN(millions/sample):</th><th> <input type="text" style="background-color:FFCCFF;color:blue;border:2px solid #CC3333;border-radius:3px" name="TO_RUN"></th>"""

    print"""<tr><th bgcolor="FF99CC" style="color:990000;">Chemistry_wrt_Machine_type:</th><th>"""
    print """<select name="Machine_type">"""

    print """<optgroup label="________________">"""
    print """<optgroup label="MISEQ">"""
    print """<optgroup label="================">"""
    print """<optgroup label=   "      v2  ">"""
    print"""<option value ="MISEQ_V2-36*1">36*1</option> """
    print"""<option value ="MISEQ_V2-25*2">25*2</option> """
    print"""<option value ="MISEQ_V2-150*2">150*2</option> """
    print"""<option value ="MISEQ_V2-250*2">250*2</option> """
    print """<optgroup label=   "      v3  ">"""
    print"""<option value ="MISEQ_V3-75*2">75*2</option> """
    print"""<option value ="MISEQ_V3-300*2">300*2</option> """
    print """<optgroup label="________________">"""

    print """<optgroup label="NEXTSEQ">"""
    print """<optgroup label="================">"""
    print """<optgroup label=   "high output  ">"""
    print"""<option value ="NEXTSEQ_HIGHOUTPUT-75*1">75*1</option> """
    print"""<option value ="NEXTSEQ_HIGHOUTPUT-75*2">75*2</option> """
    print"""<option value ="NEXTSEQ_HIGHOUTPUT-150*2">150*2</option> """
    print """<optgroup label=   "mid output  ">"""
    print"""<option value ="NEXTSEQ_MIDOUTPUT-75*2">75*1</option> """
    print"""<option value ="NEXTSEQ_MIDOUTPUT-150*2">150*2</option> """
    print """<optgroup label="________________">"""

    print """<optgroup label="  HISEQ_2500">"""
    print """<optgroup label="================">"""

    print """<optgroup label=   "high output v4  ">"""
    print"""<option value ="HISEQ2500_HIGHOUTPUT-36*1">36*1</option> """
    print"""<option value ="HISEQ2500_HIGHOUTPUT-50*2">50*2</option> """
    print"""<option value ="HISEQ2500_HIGHOUTPUT-100*2">100*2</option> """
    print"""<option value ="HISEQ2500_HIGHOUTPUT-125*2">125*2</option> """
    print """<optgroup label=   "rapid kits v2  ">"""
    print"""<option value ="HISEQ2500_RAPIDKITS-36*1">36*1</option> """
    print"""<option value ="HISEQ2500_RAPIDKITS-50*2">50*2</option> """
    print"""<option value ="HISEQ2500_RAPIDKITS-100*2">100*2</option> """
    print"""<option value ="HISEQ2500_RAPIDKITS-125*2">125*2</option> """
    print"""<option value ="HISEQ2500_RAPIDKITS-250*2">250*2</option> """
    print """<optgroup label="________________">"""

    print """<optgroup label="HISEQ_3000/4000">"""
    print """<optgroup label="================">"""
    print"""<option value ="HISEQ30004000-50*1">50*1</option> """
    print"""<option value ="HISEQ30004000-75*2">75*2</option> """
    print"""<option value ="HISEQ30004000-150*2">150*2</option> """
    print"""</select>"""
    print """</th>
             </tr>"""
    print """</table><br><br><br><br><p align="center">
             <input type="submit" value="Submit" /></p>"""    
    print '</form>'
    print '</body>'
    print '</html>'


main()
