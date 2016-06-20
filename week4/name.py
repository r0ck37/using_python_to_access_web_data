import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter - ')
count = int(raw_input('Enter count:'))
position = int(raw_input('Position: '))-1

def geturl(url,positioin):
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
        return (re.findall(r'href="(.+)"', str(tags[position])),str(tags[position].contents[0]))

print url.split("_")[-1].split(".")[0]
for x in range(count):
	result = geturl(url,position)
	url = result[0][0]
	print result[1]



