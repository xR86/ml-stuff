import urllib
import re
import json

f = urllib.urlopen("http://localhost:8000/participanti/orar_I3B5.html")
response = f.read()

# print response

"""
<tr>
    <td> 12:00</td>
    <td> 14:00</td>
    <td> Animatie 3D: algoritmi si tehnici fundamentale</td>
    <td> Seminar</td>
        <td>             <a href="../participanti/orar_vitcu.html">Conf. dr. Vitcu Anca</a>
 </td>
    <td>         <a href="../resurse/orar_C413.html">C413</a>
 </td>
        <td align="center">
&nbsp;
        </td>
    <td align="center">
         4
    </td>
    </tr>
"""

pattern = '<td> Seminar</td> <td><a .*>(.*)</a></td> <td><a .*>(.*)</a></td>'
#pattern = '<td>.*<a .*>(.*)</a></td> .* <td><a .*>(.*)</a></td>'
prog = re.compile(pattern)
matches = re.findall(pattern, response, flags=re.DOTALL)

tuples = ()
for match in matches:
    print match
