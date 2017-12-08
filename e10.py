# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e10.py          
# # Date: 01-Dec-2017  
""" Description: Find the sum of all the primes below two million."""  
sum = 0
for number in range(2, 100):
    if all(number % prime!= 0 for prime in range(2, number)):
        sum = sum + number
print sum