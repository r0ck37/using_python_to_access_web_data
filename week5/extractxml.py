#! /usr/bin/python

import urllib
import re
import xml.etree.ElementTree as ET

url = raw_input('Enter url: ') 

print 'Retriving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrived', len(data), 'characters'
tree = ET.fromstring(data)
sum = 0
i = 0 
for count in tree.findall('.//count'):
	sum += int(count.text)
	i += 1

print 'Count: ', i 
print 'Sum: ', sum
