__author__='yangyang'
def readtable(filename):
	import pprint
	infile=open(filename, 'r')
	data={}
	properties=infile.readline().split()
	for p in properties:
		data[p]={}
	#print properties

	for line in infile:
		words=line.split()
		i=int(words[0])
		values=words[1:]
		for p,v in zip(properties, values):
			if v!='no':
				data[p][i]=float(v)

	for p in properties:
		sum1=0
		for i in data[p].keys():
			sum1 += data[p][i]
		data[p]['mean']=float(sum1)/len(data[p].keys())
		#pprint.pprint(data[p]['mean'])
	data2=data.copy()
	for p in properties:

		del data2[p]['mean']
		values=data2[p].values()
		data2[p]['mean']= sum(values)/len(values)

	#print data
	print '\n'
	print data2['A']



readtable('./files/table.dat')

