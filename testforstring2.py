__author__='yangyang'
def readpair2(filename):
	infile=open(filename,'r')
	pairs = []

	for line in infile:
		line=line.strip()
		line=line.replace(' ','')
		line=line.lstrip('(')
		line=line.rstrip(')')
		line=line.replace(')(',' ')
		words=line.split()
		for word in words:
			n1=float(word.split(',')[0])
			n2=float(word.split(',')[1])
		pair=(n1,n2)
		pairs.append(pair)

	infile.close()
	print pairs


readpair2('./files/read_pairs2.dat')