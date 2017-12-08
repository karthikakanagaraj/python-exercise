# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e20.py          
# # Date: 01-Dec-2017  
""" Description:Find the sum of the digit in the number 100"""
number = 100
product = 1
while(number > 0):
	product = product * number
	number -= 1
print product
sum = 0
while(product != 0):
	reminder = product % 10
	sum = sum + reminder
	product = product / 10
print sum
