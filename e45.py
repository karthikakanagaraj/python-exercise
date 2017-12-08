# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e45.py          
# # Date: 07-Nov-2017  
""" Description:Find the next triangle number that is also pentagonal and hexagonal.""" 
p = 165
h = 143
h = 84*p + 97*h - 38
print "Next triangle number =", h*(2*h - 1)

