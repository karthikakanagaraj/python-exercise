# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e10.py          
# # Date: 01-Dec-2017  
""" Description:There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc."""
for a in range(1, 1000):  
    for b in range(a, 1000):  
        c = 1000 - a - b  
        if c*c == a*a + b*b:
        	print (a*b*c)
          