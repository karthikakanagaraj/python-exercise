# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e25.py          
# # Date: 05-Nov-2017  
""" Description:Find the index of the first term in the Fibonacci sequence to contain 1000 digits"""

from math import log10, ceil, sqrt
phi = (1+sqrt(5))/2 
d = int(input("Digits in Fibonacci number?"))
term = ceil((log10(5)/2 + d - 1) / log10(phi))
print "First term to contain %d digits is F(%d)." % (d, int(term))