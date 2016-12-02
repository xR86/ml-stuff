import urllib2,re

urlInfo = "http://profs.info.uaic.ro/~orar/orar_profesori.html"
r = re.compile("<li><a\shref=\"[^\"\.]*\.html\">.*([A-Za-z\.\s,]+)<\/a>")

try:
    response = urllib2.urlopen(urlInfo).read()
    for mo in r.finditer(response):
        print (mo.group(1).strip())
except Exception as e:
    print ("Error -> ",e)
