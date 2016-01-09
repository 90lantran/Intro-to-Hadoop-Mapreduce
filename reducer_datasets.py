#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

'''
12345"  "A"  "11"  "3"  "4"  "1"
"12345"  "B"   "6336" "Unit 1: Same Value Q"  "cs101 value same"  "question"  "\N"  "\N"  "2012-02-25 08:09:06.787181+00"  "1" 
'''
import sys
    
users = dict()
nodes = dict()

for line in sys.stdin:
	        
	if len(line) == 6:
		user_ptr_id, type,reputation, gold, silver, bronze = line
		users[user_ptr_id] = [user_ptr_id, reputation, gold, silver, bronze]
	if len(line) == 10:
		id, type, title, tagnames, author_id, none_type, parent_id, abs_parent_id, added_at = line
   		nodes[id] =[id,title,tagnames,author_id,none_type, parent_id,abs_parent_id, added_at]

for node in nodes:
	id,title,tagnames,author_id,none_type, parent_id,abs_parent_id, added_at = nodes[node]
	user_ptr_id, reputation, gold, silver, bronze = users[author_id]
	print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(iD,"B",title,tagnames,author_id,node_type,parent_id,abs_parent_id,added_at)
