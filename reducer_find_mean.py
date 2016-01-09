#!/usr/bin/python

import sys

count = [0]*7
sale = [0]*7
result = [0]*7

for line in sys.stdin:
    data = line.strip().split('\t')

    weekday, cost = data
    weekday = int(weekday)
    count[weekday] = count[weekday] + 1
    sale[weekday] = sale[weekday] + float(cost)		
    
for i in range(len(count)):
    result[i] = sale[i]
    print "{0}\t{1}".format(i,result[i])	
