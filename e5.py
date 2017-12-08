# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e5.py          
# # Date: 01-Dec-2017  
""" Description: find smallest positive number that is evenly divisible by all of the numbers from 1 to 20"""  
def gcd(x,y): return y and gcd(y, x % y) or x  
def lcm(x,y): return x * y / gcd(x,y)  
  
n = 1  
for i in range(1, 21):  
     n = lcm(n, i)  
print(n)  