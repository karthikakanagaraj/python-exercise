
# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e53.py          
# # Date: 08-Nov-2017  
"""Description:How many, not necessarily distinct, values of nCr for 1 <= n <= 100 are greater than one million"""
from math import factorial as f
# counter to count the number of instances
counter = 0

def ncr(n, r):
    return f(n)/(f(r)*f(n-r))
for n in xrange(23, 101):
    for r in xrange(4, n-3):
        if ncr(n, r) > 1000000:
            counter += 1
print counter