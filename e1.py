# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e1.py          
# # Date: 30-Nov-2017  
""" Description: find sum of multiples of 3 or 5 below 1000"""  
total = 0
for i in range(1,1000):
	if(i % 3==0 or i % 5 == 0):
		total = total + i
		print total

		