#!/usr/bin/python
import MySQLdb
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()


def main():
    SO_NUMBER = ((form["SO_NUMBER"].value).upper()).rstrip()
    CLIENT_NAME =((form["CLIENT_NAME"].value).upper()).rstrip()
    NO_OF_SAMPLE =int(form["SAMPLE_NUMBERS"].value)
    TO_RUN =float(form["TO_RUN"].value)
    Machine_Type_list =((form["Machine_type"].value).upper()).split("-")
    CHEMISTRY =Machine_Type_list[1]
    Machine_Type= Machine_Type_list[0]

    Barcode_Seq_Lis=['ATCACG', 'CGATGT', 'TTAGGC', 'TGACCA', 'ACAGTG', 'GCCAAT', 'CAGATC', 'ACTTGA', 'GATCAG', 'TAGCTT', 'GGCTAC', 'CTTGTA', 'AGTCAA', 'AGTTCC', 'ATGTCA', 'CCGTCC', 'GTAGAG', 'GTCCGC', 'GTGAAA', 'GTGGCC', 'GTTTCG', 'CGTACG', 'GAGTGG', 'GGTAGC', 'ACTGAT', 'ATGAGC', 'ATTCCT', 'CAAAAG', 'CAACTA', 'CACCGG', 'CACGAT', 'CACTCA', 'CAGGCG', 'CATGGC', 'CATTTT', 'CCAACA', 'CGGAAT', 'CTAGCT', 'CTATAC', 'CTCAGA', 'GACGAC', 'GCGCTA', 'TAATCG', 'TACAGC', 'TATAAT', 'TCATTC', 'TCCCGA', 'TCGAAG', 'TCGGCA', 'ATGCCTAA', 'GAATCTGA', 'AACGTGAT', 'CACTTCGA', 'GCCAAGAC', 'GACTAGTA', 'ATTGGCTC', 'GATGAATC', 'AGCAGGAA', 'GAGCTGAA', 'AAACATCG', 'GAGTTAGC', 'CGAACTTA', 'GATAGACA', 'AAGGACAC', 'GACAGTGC', 'ATCATTCC', 'GCCACATA', 'ACCACTGT', 'CTGGCATA', 'ACCTCCAA', 'GCGAGTAA', 'ACTATGCA', 'CGGATTGC', 'AACTCACC', 'GCTAACGA', 'CAGATCTG', 'ATCCTGTA', 'CTGTAGCC', 'GCTCGGTA', 'ACACGACC', 'AGTCACTA', 'AACGCTTA', 'GGAGAACA', 'CATCAAGT', 'AAGGTACA', 'CGCTGATC', 'GGTGCGAA', 'CCTAATCC', 'CTGAGCCA', 'AGCCATGC', 'GTACGCAA', 'AGTACAAG', 'ACATTGGC', 'ATTGAGGA', 'GTCGTAGA', 'AGAGTCAA', 'CCGACAAC', 'ACGTATCA', 'GTCTGTCA', 'CTAAGGTC', 'CGACACAC', 'CCGTGAGA', 'GTGTTCTA', 'CAATGGAA', 'AGCACCTC', 'CAGCGTTA', 'TAGGATGA', 'AGTGGTCA', 'ACAGCAGA', 'CATACCAA', 'TATCAGCA', 'ATAGCGAC', 'ACGCTCGA', 'CTCAATGA', 'TCCGTCTA', 'AGGCTAAC', 'CCATCCTC', 'AGATGTAC', 'TCTTCACA', 'CCGAAGTA', 'CGCATACA', 'AATGTTGC', 'TGAAGAGA', 'AGATCGCA', 'AAGAGATC', 'CAACCACA', 'TGGAACAA', 'CCTCTATC', 'ACAGATTC', 'CCAGTTCA', 'TGGCTTCA', 'CGACTGGA', 'CAAGACTA', 'CCTCCTGA', 'TGGTGGTA', 'AACAACCA', 'AATCCGTC', 'CAAGGAGC', 'TTCACGCA', 'CACCTTAC', 'AAGACGGA', 'ACACAGAA', 'GAACAGGC', 'AACCGAGA', 'ACAAGCTA', 'TAAGGCGA', 'CGTACTAG', 'AGGCAGAA', 'TCCTGAGC', 'GTAGAGGA', 'TAGGCATG', 'CTCTCTAC', 'CAGAGAGG', 'GCTACGCT', 'CGAGGCTG', 'AAGAGGCA', ' GGACTCCT', 'GCTCATGA', 'ATCTCAGG', 'ACTCGCTA', 'GGAGCTAC', 'GCGTAGTA', 'CGGAGCCT', 'TACGCTGC', 'ATGCGCAG', 'TAGCGCTC', 'ACTGAGCG', 'CCTAAGAC', 'CGATCAGT', 'TGCAGCTA', 'TCGACGTC']

    Barcode_Key_Lis=['NFBC07 /TSBC01', 'NFBC01 /TSBC02', 'NFBC08 /TSBC03', 'NFBC02 /TSBC04', 'NFBC03 /TSBC05', 'NFBC04 /TSBC06', 'NFBC05 /TSBC07', 'NFBC09 /TSBC08', 'NFBC10 /TSBC09', 'NFBC11 /TSBC10', 'TSBC11 /NFBC12', 'NFBC06 /TSBC12', 'NFBC13 /TSBC13', 'NFBC14 /TSBC14', 'NFBC15 /TSBC15', 'NFBC16 /TSBC16', 'NFBC17 /TSBC17', 'NFBC18 /TSBC18', 'NFBC19 /TSBC19', 'NFBC20 /TSBC20', 'NFBC21 /TSBC21', 'NFBC22 /TSBC22', 'NFBC23 /TSBC23', 'TSBC24/NFBC24', 'NFBC25 /TSBC25', 'NFBC26 /TSBC26', 'NFBC27 /TSBC27', 'NFBC28 /TSBC28', 'NFBC29 /TSBC29', 'NFBC30 /TSBC30', 'NFBC31 /TSBC31', 'NFBC32 /TSBC32', 'NFBC33 /TSBC33', 'NFBC34 /TSBC34', 'NFBC35 /TSBC35', 'NFBC36 /TSBC36', 'NFBC37 /TSBC37', 'NFBC38 /TSBC38', 'NFBC39 /TSBC39', 'NFBC40 /TSBC40','TSBC41 / N/A','N/A /NFBC41', 'NFBC42 /TSBC42', 'NFBC43 /TSBC43', 'NFBC44 /TSBC44', 'NFBC45 /TSBC45', 'NFBC46 /TSBC46', 'NFBC47 /TSBC47', 'NFBC48 /TSBC48', 'A01', 'B01', 'C01', 'D01', 'E01', 'F01', 'G01', 'H01', 'A02', 'B02', 'C02', 'D02', 'E02', 'F02', 'G02', 'H02', 'A03', 'B03', 'C03', 'D03', 'E03', 'F03', 'G03', 'H03', 'A04', 'B04', 'C04', 'D04', 'E04', 'F04', 'G04', 'H04', 'A05', 'B05', 'C05', 'D05', 'E05', 'F05', 'G05', 'H05', 'A06', 'B06', 'C06', 'D06', 'E06', 'F06', 'G06', 'H06', 'A07', 'B07', 'C07', 'D07', 'E07', 'F07', 'G07', 'H07', 'A08', 'B08', 'C08', 'D08', 'E08', 'F08', 'G08', 'H08', 'A09', 'B09', 'C09', 'D09', 'E09', 'F09', 'G09', 'H09', 'A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10', 'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11', 'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12', 'P7i1 /N701', 'P7i2 /N702', 'P7i3 /N703', 'P7i4 /N704', 'P7i5 /N712', 'P7i6 /N706', 'P7i7 /N707', 'P7i8', 'P7i9', 'P7i10 /N710', 'P7i11 /N711', 'P7i12 /N705', 'N714', 'N715', 'N716', 'N718', 'N719', 'N720', 'N721', 'N722', 'N723', 'N724', 'N726', 'N727', 'N728', 'N729']
    
    db=MySQLdb.connect("localhost", "root", "root", "Tentative_plan")
    db1= db.cursor()
    sql= "SELECT * FROM plan;"
    db1.execute(sql)
    list_barcode_db=[row[14] for row in db1.fetchall()]
    db1.execute(sql)

    print "Content-type:text/html\r\n\r\n"
    print '<html>'
    print '<head>'
    print '<title>%s</title>' % (SO_NUMBER )
    print '</head>'
    print '<body style="background-color:orange;">'
    print "HELLO!"

    if not SO_NUMBER in [row[1] for row in db1.fetchall()]:
        for i in range(NO_OF_SAMPLE):
            print(i)
            db1.execute("""insert into plan( SO_NUMBER, CLIENT_NAME, NO_OF_SAMPLE, TO_RUN, CHEMISTRY, Machine_Type) values('{}','{}',{},{},'{}', '{}')""".format(SO_NUMBER, CLIENT_NAME, NO_OF_SAMPLE, TO_RUN, CHEMISTRY, Machine_Type))
            db.commit()

        print '<form action="/cgi-bin/BarcodeToDatabase.py" method="POST">'
        print "<table cellspacing ='4'>"

        for j in range(NO_OF_SAMPLE):
            print """<tr><td><h3 style="color:green;">BARCODE_NAME:SEQ_{0}_1:</h3> <select name="BARCODE_NAME1{0}">""".format(j+1)
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
                print """<option value="{0}"> {0} : {1}</option>""".format(Barcode_Key_Lis[m], Barcode_Seq_Lis[m])

            print """</select></td><td><h3 style="color:red;">BARCODE_NAME:SEQ_{0}_2:</h3> <select name="BARCODE_NAME2{0}">""".format(j+1)
            print """<option value='NA'> NA : NA</option>"""
            for ind1, l in enumerate(Barcode_Key_Lis):
                print """<option value={0}> {0} : {1}</option>""".format(l, Barcode_Seq_Lis[ind1])

            print """</select> </td></tr>"""
        print '</table>'
        print '<input type="hidden" name="hidden" value={}>'.format(SO_NUMBER)
        print '<input type="submit" value="Submit" />'
        print '</form>'
    
    else:
        print """ <p>THE SO_NUMBER %s ASSIGNED FOR THE CLIENT %s UR TRYING TO, IS ALREADY IN THE DATABASE NAMED TENTATIVE_PLAN</p>""" % (SO_NUMBER,CLIENT_NAME)

    
    print '</body></html>'


if __name__ == "__main__":
    try:
        main()
    except KeyError:
        print "Content-type:text/html\r\n\r\n"
        print '<html>'
        print '<body style="background-color:red;">'
        print "<hr><hr><hr><br><h1>PLEASE MAKE SURE TO FURNISH ALL FIELD VALUES<h1><br><hr><hr><hr>"
        print '</body>'
        print '</html>'
    except ValueError:
        print "Content-type:text/html\r\n\r\n"
        print '<html>'
        print '<body style="background-color:red;">'
        print "<hr><hr><hr><br><h1>PLEASE ENTER CORRECT DATATYPE VALUES FOR NUMBER_OF SAMPLES(INT) AND TO_RUN(FLOAT) FIELDS <h1><br><hr><hr><hr>"
        print '</body>'
        print '</html>'

