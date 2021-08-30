#!/usr/bin/python

import MySQLdb
import cgi
import cgitb;cgitb.enable()
form = cgi.FieldStorage()
LIB_TYPE=form['LIB_TYPE'].value
BA=form['BA'].value
QUBIT=form['QUBIT'].value
qPCR= form['qPCR'].value
REPORT_NGS=form['REPORT'].value
SO_NUMBER= form['SO_NUMBER'].value
BA_TXT=form['BA_TXT'].value
DNA=form['DNA'].value
PCR_CYCLES=form['PCR_CYCLES'].value
FRAGMENT_SIZE = form['FRAGMENT_SIZE'].value
print("""Content-type: text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                 <head><title>{}</title>
                 </head>
                 <body>""".format(LIB_TYPE))

print '{},{},{},{},{},{},{},{},{}'.format(BA, QUBIT, qPCR, REPORT_NGS, SO_NUMBER, BA_TXT, DNA, PCR_CYCLES, FRAGMENT_SIZE)
print '</body>'
print '</html'


