# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e63.py          
# # Date: 07-Nov-2017  
"""Description:How many n-digit positive integers exist which are also an nth power?"""
count = 0
for number in range(1, 100):
	for power in range(1,100):
		if len(str(number ** power)) == power:
			count += 1

print count
