#!/usr/bin/python
import cgi
import MySQLdb
def htmlTop():
    print """Content-type: text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                 <head>
                     <title> tabale</title>
                 </head>
                 <body>"""
def htmlTail():
    print """ </body>
        </html>""" 
def connectDB():
    db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
    db1= db.cursor()
    return db, db1
def selectPeople(db, db1):
    sql= "SELECT * FROM plan;"
    db1.execute(sql)
    people= db1.fetchall()
    return people
def createDropDown(people):
    print """</td> <td bgcolor=#DB7093>  ID: <select name="drop">"""
    for id in people:
        print"""<option value ="{0}" > {0} </option> """.format(id[0])
    print"""</select><br>"""
def createDropDownField(fields):
    print """FIELDS: <select name= "field">"""
    for entry in fields:
        print """<option value="{0}">{0} </option>""".format(entry)
    print """</select><br>"""

def createDropDownMachine_Type(Machine_type):
    print """<form method="post" action= "machine_type.cgi">"""
    print"""<br><br><table cellspacing ='5' border='1' style="background-color:black">"""
    print"""<tr><td bgcolor=LightGreen>AMEND_MACHINE_TYPE:</td><td></td><td bgcolor=#6495ED>FROM: 
            <select name="Current_Machine_type">
            <option></option>
            <optgroup label="MISEQ">
            <option value ="MISEQ_V2">MISEQ_V2</option>
            <option value ="MISEQ_V3">MISEQ_V3</option>
            <optgroup label="NEXTSEQ">
            <option value ="NEXTSEQ_HIGHOUTPUT">NEXTSEQ_HIGHOUTPUT</option>
            <option value ="NEXTSEQ_MIDOUTPUT">NEXTSEQ_MIDOUTPUT</option>
            <optgroup label="  HISEQ_2500">
            <option value ="HISEQ2500_HIGHOUTPUT">HISEQ2500_HIGHOUTPUT</option>
            <option value ="HISEQ2500_RAPIDKITS">HISEQ2500_RAPIDKITS</option>
            <optgroup label="HISEQ_3000/4000">
            <option value ="HISEQ3000/4000">HISEQ3000/4000</option>
</select></td><td bgcolor= #6495ED>   TO: 
            <select name="Amend_Machine_type">
            <option></option>
            <optgroup label="MISEQ">
            <option value ="MISEQ_V2">MISEQ_V2</option>
            <option value ="MISEQ_V3">MISEQ_V3</option>
            <optgroup label="NEXTSEQ">
            <option value ="NEXTSEQ_HIGHOUTPUT">NEXTSEQ_HIGHOUTPUT</option>
            <option value ="NEXTSEQ_MIDOUTPUT">NEXTSEQ_MIDOUTPUT</option>
            <optgroup label="  HISEQ_2500">
            <option value ="HISEQ2500_HIGHOUTPUT">HISEQ2500_HIGHOUTPUT</option>
            <option value ="HISEQ2500_RAPIDKITS">HISEQ2500_RAPIDKITS</option>
            <optgroup label="HISEQ_3000/4000">
            <option value ="HISEQ3000/4000">HISEQ3000/4000</option></td><td>
            <input type="submit" style="background-color:#6495ED;color:blue;border:2px solid #9966FF;border-radius:5px" value="Submit" /></td></tr>"""

    print "</table>"
    print "</form><br>"

def createForm(people,fields):
    print """<form method="post" action= "UpdateDatabase.py">""" 
    print"""<table cellspacing ='9' border='1' style="background-color:black">"""
    print"""<tr>
              <td bgcolor=LightGreen>UPDATE :</td><td> """
    createDropDown(people)
    print"""</td >
              <td bgcolor=#DB7093>"""
    createDropDownField(fields)
    print"""</td>
             <td bgcolor=#DB7093>"""
    print """VALUE:<input type="text" style="background-color:#FF99CC;color:blue;border:2px solid #990000;border-radius:3px" name="testing" value=''>"""
    print """</td>
             <td>"""
    print '<input type="submit" value="Submit" style="background-color:#CD5C5C;color:blue;border:2px solid #9966FF;border-radius:5px"/>' 
    print """</td>
             </tr>"""
    print "</table>"
    print "</form>"

def sortingForm(fields):
    print """<br><form method="post" action= "SortDatabase.py">"""
    print"""<table cellspacing ='5' border='1' style="background-color:black">"""
    print"""<tr>
              <td bgcolor=LightGreen>SORT_BY:</td><td></td><td bgcolor=#FA8072>"""
    createDropDownField(fields)
    print"""</td>
             <td>"""
    print """<select name= "option">"""
    print"""<option value ="ASC" > ASC </option> """
    print"""<option value ="DESC" > DESC </option> """
    print """</td>
            <td>"""
    print '<input type="submit" value="Submit" style="background-color:#FA8072;color:blue;border:2px solid #9966FF;border-radius:5px"/>'
    print """</td>
             </tr>"""
    print "</table>"
    print "</form>"

def Auto_Machine_type():
    print """OR<br><form action="/cgi-bin/dummy.py" method="POST">
             <script type="text/javascript">
             function configureDropDownLists(county,city) {
             switch (county.value) {
             case 'MISEQ_V2':
                 document.getElementById(city).options.length = 0;
                 createOption(document.getElementById(city),15, 15);
             break;
             case 'MISEQ_V3':
                 document.getElementById(city).options.length = 0;
                 createOption(document.getElementById(city),30, 30);
             break;

             case 'HISEQ2500_HIGHOUTPUT':
                 document.getElementById(city).options.length = 0;
                 createOption(document.getElementById(city),313, 313);
             break;
             case 'HISEQ2500_RAPIDKITS':
                 document.getElementById(city).options.length = 0;
                 createOption(document.getElementById(city), 300, 300);
             break;

             case 'HISEQ30004000':
                 document.getElementById(city).options.length = 0;
                 createOption(document.getElementById(city), 300, 300);
             break;

             case 'NEXTSEQ_HIGHOUTPUT':
                 document.getElementById(city).options.length = 0;
                 createOption(document.getElementById(city),15,15);
             break;

             case 'NEXTSEQ_MIDOUTPUT':
                 document.getElementById(city).options.length = 0;
                 createOption(document.getElementById(city),130,130);
             break;

                  }
             }

            function createOption(county, text, value) {
            var opt = document.createElement('option');
            opt.value = value;
            opt.text = text;
            county.options.add(opt);
            }
            </script><table cellspacing ='9' border='1' style="background-color:black"><tr><td  bgcolor=LightGreen>MACHINE_TYPE:</td>
            <td></td><td bgcolor=FF1493>MACHINE_TYPE:<select name="MACHINE_TYPE" id="county" onchange="configureDropDownLists(this,'city');">

            <option></option>
            <optgroup label="MISEQ">
            <option value ="MISEQ_V2">MISEQ_V2</option>
            <option value ="MISEQ_V3">MISEQ_V3</option>
            <optgroup label="NEXTSEQ">
            <option value ="NEXTSEQ_HIGHOUTPUT">NEXTSEQ_HIGHOUTPUT</option>
            <option value ="NEXTSEQ_MIDOUTPUT">NEXTSEQ_MIDOUTPUT</option>
            <optgroup label="  HISEQ_2500">
            <option value ="HISEQ2500_HIGHOUTPUT">HISEQ2500_HIGHOUTPUT</option>
            <option value ="HISEQ2500_RAPIDKITS">HISEQ2500_RAPIDKITS</option>
            <optgroup label="HISEQ_3000/4000">
            <option value ="HISEQ30004000">HISEQ3000/4000</option>

            </select></td>
            <td bgcolor=FF1493>TO_RUN_SUM:<select name="SUM" id="city">
            </select></td>
            <td><input type="submit" value="Submit" style="background-color:#FF1493;color:blue;border:2px solid #9966FF;border-radius:5px" /></td>
            </tr></table></form>"""

def groupForm(fields):
    print """<br><br><form method="post" action= "FilterDatabase.py">"""
    print"""<table cellspacing ='5' border='1' style="background-color:black">"""
    print"""<tr>
              <td bgcolor=FF4500>FILTER_BY:</td><tr><td bgcolor=LightGreen>MANUAL_ENTRY:</td><td bgcolor=#DA70D6> """
    createDropDownField(fields)
    print"""</td>
             <td bgcolor= #DA70D6>"""
    print """FIELD_VALUE:<input type="text" style="background-color:#00FFFF;color:990000;border-radius:5px; border:2px solid #CC6699" name="field_value">"""
    print """</td>
             <td bgcolor= #DA70D6>TO_RUN_SUM:"""
    print """<input type="text" style="background-color:#00FFFF;color:990000;border-radius:5px; border:2px solid #CC6699" name="summ_value" value=''>"""
    print """</td>
            <td>"""
    print '<input type="submit" value="Submit"  style="background-color:#DA70D6;color:blue;border:2px solid #9966FF;border-radius:5px"/>'
    print """</td>
             </tr>"""
    print "</table>"
    print "</form>"     
 
def displayPeople(people):
    print "<table border= '1'>"
    print "<tr>"
    print "<th bgcolor=FF00CC>ID</th>"
    print "<th bgcolor=FF00CC>SO_NUMBER</th>"
    print "<th bgcolor=FF00CC>SAMPLE_ID</th>"
    print "<th bgcolor=FF00CC>CLIENT_NAME</th>"
    print "<th bgcolor=FF00CC>NO_OF_SAMPLE</th>"
    print "<th bgcolor=FF00CC>ORGANISM</th>"
    print "<th bgcolor=FF00CC>CHEMISTRY</th>"
    print "<th bgcolor=FF00CC>APPLICATION</th>"
    print "<th bgcolor=FF00CC>MIN_READS</th>"
    print "<th bgcolor=FF00CC>MAX_READS</th>"
    print "<th bgcolor=FF00CC>TO_RUN</th>"
    print "<th bgcolor=FF00CC>AVG_SIZE</th>"
    print "<th bgcolor=FF00CC>AVERAGE_NM</th>"
    print "<th bgcolor=FF00CC>QUBIT_NG</th>"
    print "<th bgcolor=FF00CC>BARCODE_NAME1</th>"
    print "<th bgcolor=FF00CC>BARCODE_SEQ1</th>"
    print "<th bgcolor=FF00CC>BARCODE_SEQ2</th>"
    print "<th bgcolor=FF00CC>BARCODE_NAME2</th>"
    print "<th bgcolor=FF00CC>Machine_Type</th>"
    print "</tr>"
    for each in people:
        print "<tr>"
        print "<td bgcolor=55ff55>{0} </td>".format(each[0])
	print "<td bgcolor=55ff55>{0} </td>".format(each[1])
	print "<td bgcolor=55ff55>{0} </td>".format(each[2])
	print "<td bgcolor=55ff55>{0} </td>".format(each[3])
        print "<td bgcolor=55ff55>{0} </td>".format(each[4])
        print "<td bgcolor=55ff55>{0} </td>".format(each[5])
        print "<td bgcolor=55ff55>{0} </td>".format(each[6])
        print "<td bgcolor=55ff55>{0} </td>".format(each[7])
        print "<td bgcolor=55ff55>{0} </td>".format(each[8])
        print "<td bgcolor=55ff55>{0} </td>".format(each[9])
        print "<td bgcolor=55ff55>{0} </td>".format(each[10])
        print "<td bgcolor=55ff55>{0} </td>".format(each[11])
        print "<td bgcolor=55ff55>{0} </td>".format(each[12])
        print "<td bgcolor=55ff55>{0} </td>".format(each[13])
        print "<td bgcolor=55ff55>{0} </td>".format(each[14])
        print "<td bgcolor=55ff55>{0} </td>".format(each[15])
        print "<td bgcolor=55ff55>{0} </td>".format(each[16])
        print "<td bgcolor=55ff55>{0} </td>".format(each[17])
        print "<td bgcolor=55ff55>{0} </td>".format(each[18])
        print "</tr>"
    print "</table><br>"

def xl(people):
    import xlwt
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('final_plan')
    header=['ID', 'SO_NUMBER', 'SAMPLE_ID', 'CLIENT', 'NO_OF_SAMPLE', 'ORGANISM', 'CHEMISTRY', 'APPLICATION', 'MIN_READS', 'MAX_READS', 'TO_RUN', 'AVG_SIZE', 'AVERAGE_NM', 'QUBIT_NG', 'BARCODE_NAME1', 'BARCODE_SEQ1', 'BARCODE_SEQ2', 'BARCODE_NAME2', 'MACHINE_TYPE']
    for index, value in enumerate(header):
        worksheet.write(0, index, value)

    for row_index, row_value in enumerate(people):
        for col_index, col_value in enumerate(row_value):
            worksheet.write(row_index+1, col_index, col_value)

    workbook.save('TENTATIVE_PLAN.xls')

def button():
    print """<br><br><hr>Download_Tentative_plan: <a href="//localhost/TENTATIVE_PLAN.xls" class="button">
                   Dowload_XLS_FILE!
                        </a><br>"""

def databasedump():
    import os
    target_dir = '/var/www/cgi-bin/'
    os.system("mysqldump --add-drop-table -c -u root -proot 'Tentative_plan' > "+target_dir+"database.bak.sql")


def Delete_Multiplerows(people):
    print """<br><form method="post" action= "Delete_Rows.py">"""
    print"<table cellspacing ='4' border='3'>"
    print"""<tr><td>DELETE MULTIPLE ROWS BY SELECTING ID : </td>
              <td bgcolor=55ff55><select name="Delete_Rows" multiple>""" 
    for id in people:
        print"""<option value ="{0}" > {0} </option> """.format(id[0])

    print"""</select></td><td><input type="submit" value="Submit" /></td></tr>"""


if __name__ == "__main__":
    try:
        htmlTop()
        db, db1 =connectDB()
        people = selectPeople(db,db1)
        db1.close()
        displayPeople(people)
        xl(people)
        fields=['SO_NUMBER','SAMPLE_ID','CLIENT_NAME','NO_OF_SAMPLE','ORGANISM','CHEMISTRY','APPLICATION', 'MIN_READS','MAX_READS','TO_RUN', 'AVG_SIZE', 'AVERAGE_NM','QUBIT_NG','BARCODE_NAME1', 'BARCODE_SEQ1','BARCODE_SEQ2', 'BARCODE_NAME2' ]
        sort_element=['ID','SO_NUMBER','SAMPLE_ID','CLIENT_NAME','NO_OF_SAMPLE','ORGANISM','CHEMISTRY','APPLICATION', 'MIN_READS','MAX_READS','TO_RUN', 'AVG_SIZE', 'AVERAGE_NM','QUBIT_NG','BARCODE_NAME1', 'BARCODE_SEQ1','BARCODE_SEQ2', 'BARCODE_NAME2' ]
        Machine_type=['a','b','c','d','f','g','h']
        createForm(people,fields)
        createDropDownMachine_Type(Machine_type)
        sortingForm(sort_element)
        groupForm(fields)
        Auto_Machine_type()
        button()
        databasedump()
        Delete_Multiplerows(people)
        htmlTail()
    except:
        cgi.print_exception()   

