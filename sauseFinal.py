import sys
from bs4 import BeautifulSoup
import urllib2
def beauty(s,x):
	for i in range(1,x) :
		print s,
	return
if(sys.argv[-1]!=sys.argv[0]):
	 var=str(sys.argv[-1])
else:   var='-'
size=50	
beauty(var,size)
print
print var+'\t\tName \t\t\t   Long \tCookoff \tLTime ALL\t\t'+var
print var+'\t\t   \t \t\tCountry Global Global Country Global Country\t\t' +var
beauty(var,size)
print

for i in open("username.txt"):
	r=map(str,i.split())
	#if(sys.argv[-1]!=sys.argv[0]):
	#	var=str(sys.argv[-1])
	#else:	var='-
	size=50
	for x in r:
                
		url="http://www.codechef.com/users/" +x
                content=urllib2.urlopen(url).read()
                soup = BeautifulSoup(content)
                beauty(var +'\t\t',2)
                print x,
                if(len(x)<=6): beauty('\t\t\t',2)
		else:	beauty("\t\t",2)
                y=soup.find_all('hx')
                for links in y:
                        k=links.get_text()
                        if(k==''): print "NA",
                        else:   print k ,
                        print ("\t"),
                beauty('\t'+var,2)
                print
        beauty(var,size)
	print


