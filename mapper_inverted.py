#!/usr/bin/python

import sys
import re
import csv


#reader = csv.reader(sys.stdin, delimiter='\t')
#writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

#regex = re.compile("\bfantastic\b")
#for line in reader:
    #print line
#    match = regex.findall(line[4],re.IGNORECASE)
#    if len(match) > 0:		
    	
#    	print ("{0}\t{1}".format(match[0], len(match)))
  
    #data = re.split(c,line)
    #data = re.split('\t| |\. |\n|, |!|?',line)
    #print data
#with open('test1.csv', 'wb') as testfile:
 #   csv_writer = csv.writer(testfile)

  #  for line in sys.stdin:
   #   	line.replace('\n',"gsdhghsaghjash")
#	csv_writer.writerow(line)
#	print line	
    

reader = csv.reader(sys.stdin, delimiter='\t')
delimiters = ['.',',','$',';','!','?',':','"','(',')','[',']','<','>','#','=','-','/',' ']

regex = '|'.join(map(re.escape, delimiters))

for line in reader:
    #print line   		
    node_id = line[0]
    if node_id == "id":
	continue
    body = re.split(regex, line[4])

    for token in body:
    	print "{0}\t{1}".format(node_id, token)
















