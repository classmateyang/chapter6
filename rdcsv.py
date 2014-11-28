__author__='yangyang'
import csv
import pprint

localfile='./files/budget.csv'
infile=open(localfile,'r')
table=[]

for row in csv.reader(infile):
	table.append(row)
infile.close()

#pprint.pprint(table)
'''
for r in range(1,len(table)):
	for c in range(1,len(table[0])):
		table[r][c]=float(table[r][c])
'''
#pprint.pprint(table)

for r in table[1:]:
	for c in r[1:]:
		table[table.index(r)][r.index(c)]=float(c)


row=[0.0]*len(table[0])
for c in range(1,len(row)):
	s=0
	for r in range(1,len(table)):
		s +=table[r][c]
	row[c]=s
row[0]='total'


table.append(row)


outfile=open('budget11.csv','w')
writer=csv.writer(outfile)
for row in table:
	writer.writerow(row)
outfile.close()
