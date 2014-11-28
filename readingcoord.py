__author__='yangyang'
import numpy as np

def readcord(filename):
	infile=open(filename,'r')
	coords = []
	for line in infile:
		x_start=line.find('x=')
		y_start=line.find('y=')
		z_start=line.find('z=')
		xstring=line[x_start+2:y_start]
		ystring=line[y_start+2:z_start]
		zstring=line[z_start+2:]
		cord=(float(xstring),float(ystring),float(zstring))
		coords.append(cord)

	infile.close()
	arraycoords=np.array(coords)

	print arraycoords

	print arraycoords.shape




readcord('./files/xyz.dat')