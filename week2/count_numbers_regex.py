#!/usr/bin/python3

from sys import argv
import re

script, filename = argv

txt = open(filename)
sum = 0

for line in txt:
    data = [int(x) for x in re.findall(r"\d+", line)]
    for value in data:
        sum += value

print (sum)

txt.close()
