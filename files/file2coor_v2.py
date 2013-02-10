infile = open('xyz.dat', 'r')
coor = []  # list of (x,y,z) tuples
for line in infile:
    x_start = line.find('x=')
    y_start = line.find('y=')
    z_start = line.find('z=')
    x = line[x_start+2:y_start]
    y = line[y_start+2:z_start]
    z = line[z_start+2:]
    print 'debug: x="%s", y="%s", z="%s"' % (x,y,z)
    coor.append((float(x), float(y), float(z)))
infile.close()

import numpy as np
coor = np.array(coor)
print coor.shape, coor

