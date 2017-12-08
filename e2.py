# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e2.py          
# # Date: 30-Nov-2017  
""" Description:Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""  
a,b=0,1
c=0
sum=0
for i in range (50):
	c=a+b
	a=b
	b=c
	if c<4000000:
		print c
		sum = sum+c if c%2 ==0 else sum+0
		print sum
