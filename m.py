#!/usr/bin/python
import sys
import csv
import re


reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
   
    words = re.findall(r"[\w']+", line[4])
    words = map(lambda x: x.lower(), words)
	# if "fantastically" in words:
	# writer.writerow(line)
    for word in words:
	print word, '\t', line[0]
