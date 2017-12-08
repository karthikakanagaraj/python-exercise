# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e48.py          
# # Date: 01-Dec-2017  
""" Description:Find the last ten digits of the series, 1 pow1 + 2pow2 + 3pow3 + ... + 1000pow1000."""
sum = 0
count = 0
for product in range(1, 1001):
	sum = sum + (product ** product)
#print sum
while(count <= 10):
	reminder = sum % 10
	count += 1
	sum = sum / 10
	print (str(reminder)[0:10])

