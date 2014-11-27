__author__='yangyang'
def readpair3(filename):
	infile=open(filename,'r')
	pairs = []
	listtext='['
	for line in infile:
		line=line.strip()

		listtext +=line+','
	infile.close()

	listtext =listtext[:-1] +']'
	pairs=eval(listtext)
	print pairs


readpair3('./files/read_pairs3.dat')