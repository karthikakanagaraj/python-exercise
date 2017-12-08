# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e10.py          
# # Date: 01-Dec-2017  
""" Description:Sum of the digit of the number 2 power 1000"""
base = 2
exponent = 1000
power = 1
for product in range(1, exponent + 1):
	power = power * base
print power
sum = 0	
while(power != 0):
	reminder = power % 10
	sum = sum + reminder
	power = power / 10
print sum

