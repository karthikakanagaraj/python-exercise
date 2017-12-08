# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e4.py          
# # Date: 30-Nov-2017    
"""Description:The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum"""
sum1=0
for i in range(1,101):
	sum1+=(i*i)
	num=0
	for j in range(1,101):
		num=num+j
		sum2=num*num
		print sum2
		c=sum2-sum1
		print c