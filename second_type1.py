#!/usr/bin/python
import cgi
import cgitb;cgitb.enable()
form = cgi.FieldStorage()
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<body>hello!<br>'
print"""<form method="post" action= "second_type1_1.py">
            <br>
            ENTER_SO_#: <input type="text" style="background-color:00FFCC;color:blue;border:2px solid #9966FF;border-radius:5px"  name="SO_NUMBER"><br><br>
            PROJECT_OBJECTIVES: <br><textarea rows="6" cols="120" style="background-color:00FFCC;color:blue;border:2px solid #9966FF;border-radius:10px" name="OBJECTIVE"></textarea><br><br>
             PROJECT_TYPE:<SELECT name="project_type">
                          <optgroup label="WGS">
                          <option value="WGS_REFSEQ">REFSEQ</option>
                          <option value="WGS_DENOVO">DENOVO</option>
                          </optgroup>
                          <optgroup label="SMALL_RNA">
                          <option value="SMALL_RNA">SMALL_RNA</option>
                          </optgroup>
                          <optgroup label="BACTERIAL_DNA_WGS">
                          <option value="BACTERIAL_DNA_WGS_DENOVO">DENOVO</option>
                          <option value="BACTERIAL_DNA_WGS_ANA">ANA</option>
                          </optgroup>
                          <optgroup label="RNA_SEQ">
                          <option value="RNA_SEQ_DENOVO">DENOVO</option>
                          <option value="RNA_SEQ_TXOME_REFSEQ">TXOME_REFSEQ</option>
                          </optgroup>
             </select> """
print """<input type="submit" value="Submit" /></form>"""
print '</body>'
print '</html>'
