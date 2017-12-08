# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e30.py          
# # Date: 05-Nov-2017  
""" Description: Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""
sum = 0
number = 1634
number1 = number
while(number1 != 0):
	reminder = number1 % 10
	sum = sum + (reminder ** 4)
	number1 = number1 / 10
print sum
if(sum == number):
	print sum
else:
	print 0
	
	