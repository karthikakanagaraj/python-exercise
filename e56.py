# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e56.py          
# # Date: 06-Nov-2017  
"""Description:Considering natural numbers of the form, aa pow b where a, b < 100, what is the maximum digital sum?"""

print "Maximum digital sum =",
print max(sum(map(int, str(a**b))) for a in xrange(60, 100) for b in xrange(80, 100))