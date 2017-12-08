# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e24.py          
# # Date: 05-Nov-2017  
""" Description: What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""

from itertools import permutations
lexi_perm = list(permutations('0123456789'))
solution = ''.join(lexi_perm[999999])
print solution
