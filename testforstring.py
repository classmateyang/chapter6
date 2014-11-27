__author__='yangyang'
def readpair1(filename):
	infile=open(filename,'r')
	pairs = []
	for line in infile:
		words=line.split()#words is a list of string
		for word in words:#word is of the type string
			word = word[1:-1].split(',')#get rid of the bracket in the pairs and split with the delimeter','
			n1 = float(word[0])#convert the string to a float number
			n2 = float(word[1])#convert the string to a float number
			pair = (n1, n2) #put the pair of numbers into a turpl
			pairs.append(pair)#add the turpl elements to the pairs list
	infile.close()
	print pairs


readpair1('./files/read_pairs1.dat')
