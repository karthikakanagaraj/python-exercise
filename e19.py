# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e19.py          
# # Date: 01-Dec-2017  
""" Description:How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""
import datetime
#import cProfile
count = 0
for y in range(1901, 2001):
	for m in range(1, 13):
		if datetime.datetime(y, m, 1).weekday() == 6:
			count += 1
print(count)
   



