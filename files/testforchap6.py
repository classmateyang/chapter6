__author__='yangyang'
#temps={'Oslo':13, 'Londo':15.4, 'Paris':17.5,'Beijing':19}
def red_densities(filename):
	import pprint

	infile=open(filename, 'r')
	densities={}
	for line in infile:
		words =line.split()
		density=float(words[-1])
		if len(words)==2:
			substance=words[0]
		else:
			substance=words[0]+' '+words[1]
		densities[substance]=density
	pprint.pprint(densities)


red_densities('densities.dat')