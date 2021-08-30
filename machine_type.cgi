#!/usr/bin/python
import MySQLdb
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()

def main():
    Current_Machine_type = (form["Current_Machine_type"].value).upper()
    Amend_Machine_type =(form["Amend_Machine_type"].value).upper()
    print "Content-type:text/html\r\n\r\n"
    print '<html>'
    print '<head>'
    print '<title>CHANG_OF_MACHINE_TYPE</title>'
    print '<body>{},{}'.format(Current_Machine_type, Amend_Machine_type)


    db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
    db1= db.cursor()
    sql= "SELECT * FROM plan WHERE Machine_Type ='{}';".format(Current_Machine_type)
    db1.execute(sql)
    people= db1.fetchall()

    sql1= "SELECT * FROM plan WHERE Machine_Type ='{}';".format(Amend_Machine_type)
    db1.execute(sql1)
    list_barcode_db=[row[14] for row in db1.fetchall()]

    Barcode_Seq_Lis=['ATCACG', 'CGATGT', 'TTAGGC', 'TGACCA', 'ACAGTG', 'GCCAAT', 'CAGATC', 'ACTTGA', 'GATCAG', 'TAGCTT', 'GGCTAC', 'CTTGTA', 'AGTCAA', 'AGTTCC', 'ATGTCA', 'CCGTCC', 'GTAGAG', 'GTCCGC', 'GTGAAA', 'GTGGCC', 'GTTTCG', 'CGTACG', 'GAGTGG', 'GGTAGC', 'ACTGAT', 'ATGAGC', 'ATTCCT', 'CAAAAG', 'CAACTA', 'CACCGG', 'CACGAT', 'CACTCA', 'CAGGCG', 'CATGGC', 'CATTTT', 'CCAACA', 'CGGAAT', 'CTAGCT', 'CTATAC', 'CTCAGA', 'GACGAC', 'GCGCTA', 'TAATCG', 'TACAGC', 'TATAAT', 'TCATTC', 'TCCCGA', 'TCGAAG', 'TCGGCA', 'ATGCCTAA', 'GAATCTGA', 'AACGTGAT', 'CACTTCGA', 'GCCAAGAC', 'GACTAGTA', 'ATTGGCTC', 'GATGAATC', 'AGCAGGAA', 'GAGCTGAA', 'AAACATCG', 'GAGTTAGC', 'CGAACTTA', 'GATAGACA', 'AAGGACAC', 'GACAGTGC', 'ATCATTCC', 'GCCACATA', 'ACCACTGT', 'CTGGCATA', 'ACCTCCAA', 'GCGAGTAA', 'ACTATGCA', 'CGGATTGC', 'AACTCACC', 'GCTAACGA', 'CAGATCTG', 'ATCCTGTA', 'CTGTAGCC', 'GCTCGGTA', 'ACACGACC', 'AGTCACTA', 'AACGCTTA', 'GGAGAACA', 'CATCAAGT', 'AAGGTACA', 'CGCTGATC', 'GGTGCGAA', 'CCTAATCC', 'CTGAGCCA', 'AGCCATGC', 'GTACGCAA', 'AGTACAAG', 'ACATTGGC', 'ATTGAGGA', 'GTCGTAGA', 'AGAGTCAA', 'CCGACAAC', 'ACGTATCA', 'GTCTGTCA', 'CTAAGGTC', 'CGACACAC', 'CCGTGAGA', 'GTGTTCTA', 'CAATGGAA', 'AGCACCTC', 'CAGCGTTA', 'TAGGATGA', 'AGTGGTCA', 'ACAGCAGA', 'CATACCAA', 'TATCAGCA', 'ATAGCGAC', 'ACGCTCGA', 'CTCAATGA', 'TCCGTCTA', 'AGGCTAAC', 'CCATCCTC', 'AGATGTAC', 'TCTTCACA', 'CCGAAGTA', 'CGCATACA', 'AATGTTGC', 'TGAAGAGA', 'AGATCGCA', 'AAGAGATC', 'CAACCACA', 'TGGAACAA', 'CCTCTATC', 'ACAGATTC', 'CCAGTTCA', 'TGGCTTCA', 'CGACTGGA', 'CAAGACTA', 'CCTCCTGA', 'TGGTGGTA', 'AACAACCA', 'AATCCGTC', 'CAAGGAGC', 'TTCACGCA', 'CACCTTAC', 'AAGACGGA', 'ACACAGAA', 'GAACAGGC', 'AACCGAGA', 'ACAAGCTA', 'TAAGGCGA', 'CGTACTAG', 'AGGCAGAA', 'TCCTGAGC', 'GTAGAGGA', 'TAGGCATG', 'CTCTCTAC', 'CAGAGAGG', 'GCTACGCT', 'CGAGGCTG', 'AAGAGGCA', ' GGACTCCT', 'GCTCATGA', 'ATCTCAGG', 'ACTCGCTA', 'GGAGCTAC', 'GCGTAGTA', 'CGGAGCCT', 'TACGCTGC', 'ATGCGCAG', 'TAGCGCTC', 'ACTGAGCG', 'CCTAAGAC', 'CGATCAGT', 'TGCAGCTA', 'TCGACGTC']

    Barcode_Key_Lis=['NFBC07 /TSBC01', 'NFBC01 /TSBC02', 'NFBC08 /TSBC03', 'NFBC02 /TSBC04', 'NFBC03 /TSBC05', 'NFBC04 /TSBC06', 'NFBC05 /TSBC07', 'NFBC09 /TSBC08', 'NFBC10 /TSBC09', 'NFBC11 /TSBC10', 'TSBC11 /NFBC12', 'NFBC06 /TSBC12', 'NFBC13 /TSBC13', 'NFBC14 /TSBC14', 'NFBC15 /TSBC15', 'NFBC16 /TSBC16', 'NFBC17 /TSBC17', 'NFBC18 /TSBC18', 'NFBC19 /TSBC19', 'NFBC20 /TSBC20', 'NFBC21 /TSBC21', 'NFBC22 /TSBC22', 'NFBC23 /TSBC23', 'TSBC24/NFBC24', 'NFBC25 /TSBC25', 'NFBC26 /TSBC26', 'NFBC27 /TSBC27', 'NFBC28 /TSBC28', 'NFBC29 /TSBC29', 'NFBC30 /TSBC30', 'NFBC31 /TSBC31', 'NFBC32 /TSBC32', 'NFBC33 /TSBC33', 'NFBC34 /TSBC34', 'NFBC35 /TSBC35', 'NFBC36 /TSBC36', 'NFBC37 /TSBC37', 'NFBC38 /TSBC38', 'NFBC39 /TSBC39', 'NFBC40 /TSBC40','TSBC41 / N/A','N/A /NFBC41', 'NFBC42 /TSBC42', 'NFBC43 /TSBC43', 'NFBC44 /TSBC44', 'NFBC45 /TSBC45', 'NFBC46 /TSBC46', 'NFBC47 /TSBC47', 'NFBC48 /TSBC48', 'A01', 'B01', 'C01', 'D01', 'E01', 'F01', 'G01', 'H01', 'A02', 'B02', 'C02', 'D02', 'E02', 'F02', 'G02', 'H02', 'A03', 'B03', 'C03', 'D03', 'E03', 'F03', 'G03', 'H03', 'A04', 'B04', 'C04', 'D04', 'E04', 'F04', 'G04', 'H04', 'A05', 'B05', 'C05', 'D05', 'E05', 'F05', 'G05', 'H05', 'A06', 'B06', 'C06', 'D06', 'E06', 'F06', 'G06', 'H06', 'A07', 'B07', 'C07', 'D07', 'E07', 'F07', 'G07', 'H07', 'A08', 'B08', 'C08', 'D08', 'E08', 'F08', 'G08', 'H08', 'A09', 'B09', 'C09', 'D09', 'E09', 'F09', 'G09', 'H09', 'A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10', 'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11', 'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12', 'P7i1 /N701', 'P7i2 /N702', 'P7i3 /N703', 'P7i4 /N704', 'P7i5 /N712', 'P7i6 /N706', 'P7i7 /N707', 'P7i8', 'P7i9', 'P7i10 /N710', 'P7i11 /N711', 'P7i12 /N705', 'N714', 'N715', 'N716', 'N718', 'N719', 'N720', 'N721', 'N722', 'N723', 'N724', 'N726', 'N727', 'N728', 'N729']


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

    print """<form method="post" action= "Machine_Amend.py">"""
    print"<table cellspacing ='5'>"
    print"""<tr>MULTIPLE_SELECTION_OPTION_FOR_CHANGING_MACHINE_TYPE<td>ID: </td>
              <td bgcolor=55ff55><select name="drop" multiple>""" 
    for id in people:
        print"""<option value ="{0}" > {0} </option> """.format(id[0])

    print"""</select>"""
    print"""</td ><td>BARCODE_NAME_AND_SEQ1</td><td><select name="BARCODE_NAME_AND_SEQ1" multiple>"""
    print """<optgroup label="NFBC/TSBC">"""
    for k in range(49):
        if not Barcode_Key_Lis[k] in list_barcode_db:
            print """<option value="{0}"> {0} : {1}</option>""".format(Barcode_Key_Lis[k], Barcode_Seq_Lis[k])
    print """<optgroup label="Agilent_BC">"""
    for l in range(49, 145):
        if not Barcode_Key_Lis[l] in list_barcode_db:
            print """<option value="{0}"> {0} : {1}</option>""".format(Barcode_Key_Lis[l], Barcode_Seq_Lis[l])

    print """<optgroup label="Agilent_SureSelect/Nextera_XT">"""
    for m in range(145, 171):
        if not Barcode_Key_Lis[m] in list_barcode_db:
            print """<option value="{0}"> {0} : {1}</option>""".format(Barcode_Key_Lis[m], Barcode_Seq_Lis[m])

    print """</select></td><td><input type="hidden" name="hidden" value={}><input type="submit" value="Submit" /></td></tr>""".format(Amend_Machine_type)
    print "</form>"
    print '</body>'
    print '</html>'


if __name__ == "__main__":
    try:
        main()
    except KeyError:
        print "Content-type:text/html\r\n\r\n"
        print '<html>'
        print '<body style="background-color:red;">'
        print "<hr><hr><hr><br>SELECT MACHINE TYPES TO AMEND<br><br><hr><hr><hr>"
        print '</body>'
        print '</html>'

