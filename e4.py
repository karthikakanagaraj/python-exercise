# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e4.py          
# # Date: 30-Nov-2017    
"""Description: Largest palindrome made from the product of two three digit numbers."""

a=999
b=100
for i in range (1000):
	c=a*b
	if int(str(c)[::-1]) == c:
		print c
		a=a-1
		
		
