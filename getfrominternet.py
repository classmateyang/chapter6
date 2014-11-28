__author__='yangyang'
import urllib
url=\
'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/oxforddata.txt'
urllib.urlretrieve(url, filename='oxfordweather.txt')

infile = open('oxfordweather.txt','r')


data = {}
data['place'] = infile.readline().strip()
data['location'] = infile.readline().strip()
# Skip the next 5 lines
for i in range(5):
    infile.readline()

data['data'] ={}

for line in infile:
	columns = line.split()
	year = int(columns[0])
	month = int(columns[1])

	if columns[-1]=='Provisional':
		del columns[-1]
	for i in range(2,len(columns)):
		if columns[i]=='---':
			columns[i]=None
		elif columns[i][-1]=='#' or columns[i][-1]=='*':
			columns[i]=float(columns[i][:-1])
		else:
			columns[i]=float(columns[i])
	tmax, tmin, air_frost, rain, sun=columns[2:]
	if not year in data['data']:
		data['data'][year]={}
	data['data'][year][month]={'tmax': tmax, 'tmin': tmin, 'air frost': air_frost, 'sun': sun}


infile.close()

