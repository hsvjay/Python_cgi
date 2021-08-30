#!/usr/bin/python
import cgi
keyword= "Welcome_to_Report_AUTOMATION"
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>%s</title>' % ( keyword )
print '<body>'
print "Hello"


print '<form action="/cgi-bin/dummy.py" method="POST">'
print """<script type="text/javascript">


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

case "HISEQ_3000/4000":
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
</script><tr>
<td>Machine_Type: </td>
<td><select name="MACHINE_TYPE" id="county" onchange="configureDropDownLists(this,'city');">


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

</select></td>
<td>TO_RUN_SUM: </td>
<td><select name="SUM" id="city">
</select></td>
<td><input type="submit" value="Submit" /></td>
</tr>"""

print '</form>'

              
print '</body>'
print '</html>'
