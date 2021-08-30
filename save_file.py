#!/usr/bin/python
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
# Get filename here.
hid=form['hidden'].value
fileitem = form['PRS']
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'
   
print """\
Content-Type: text/html\n
<html>
<body>	
   <p>fileitem</p>
   <p>%s%s</p>
</body>
</html>
""" % (message,fn,)
#connecting_to_count_the_no_samples
#Number_of_samples=''
filepathname= '/tmp/'+ fn
# list_of_samples= zip(*Read_file(filepathname, Number_of_samples))[1]
# ADD_TO_DATABASE
print """\
<html> 
  <head> 
    <meta http-equiv="refresh" content="5;url=http://localhost/common.cgi?SO_NUMBER={}" /> 
    <title>You are going to be redirected {}</title> 
  </head> 
  <body> 
    Redirecting...
  </body> 
</html> """.format(hid,filepathname)

def Read_file(filepath,Number_of_samples):
    import csv
    row_list=[]
    with open(filepath,'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i, row in enumerate(spamreader):
            if (i>0) and (i<1+int(Number_of_samples)):
                row_list.append(row)
    return row_list
