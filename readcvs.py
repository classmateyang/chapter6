__author__='yangyang'
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter, DayLocator

def readcvs(filename):
	import pprint

	infile=open(filename, 'r')

	properties=infile.readline().split(',')

	properties=properties[:-1] + properties[-1].split()

	#print properties
	dates=[]
	prices=[]
	for line in infile:
		words=line.split(',')
		dates.append(words[0])
		prices.append(float(words[-1]))
	infile.close()

	dates.reverse()
	prices.reverse()
	# pprint.pprint(dates)
	#pprint.pprint(prices)

	datefmt='%Y-%m-%d'
	dates=[datetime.strptime(_date, datefmt).date() for _date in dates]
	prices=np.array(prices)
	#pprint.pprint(prices)
	#pprint.pprint(dates)

	return dates[1:], prices[1:]
'''
dates={}
prices={}
import glob
filenames=glob.glob('./files/stockprices_*.csv')


for filename in filenames:
	company=filename[20:-4]
	d, p = readcvs(filename)

	dates[company]=d
	prices[company]=p

print dates['Google']
print prices['Google']

'''
d, p = readcvs('tablemicsft.csv')

company='Microsoft'
normalizedprice=[price/p[0] for price in p]
fig, ax = plt.subplots()
ax.plot_date(d, np.log(normalizedprice), '-', label=company)

plt.legend(company, loc='upper left')
ax.set_ylabel('logarithm of price value')
ax.set_xlabel('Time')

months = MonthLocator(1)
days = DayLocator(30)
years = YearLocator(1)
daysfmt = DateFormatter('%d')
monthsfmt = DateFormatter('%m')
yearsfmt = DateFormatter('%Y')
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsfmt)
ax.xaxis.set_minor_locator(days)
ax.xaxis.set_minor_formatter(daysfmt)
ax.autoscale_view()
fig.autofmt_xdate()
plt.show()
'''

company='Microsoft'
fig, ax = plt.subplots()
legends = []

ax.plot_date(d, np.log(normalizedprice), '-', label=company)
legends.append(company)
ax.legend(legends, loc='upper left')
ax.set_ylabel('logarithm of price value')
ax.set_xlabel('Time')
# Format the ticks
years    = YearLocator(5)   # major ticks every 5 years
months   = MonthLocator(6)  # minor ticks every 6 months
yearsfmt = DateFormatter('%Y')
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsfmt)
ax.xaxis.set_minor_locator(months)
ax.autoscale_view()
fig.autofmt_xdate()
plt.show()
'''