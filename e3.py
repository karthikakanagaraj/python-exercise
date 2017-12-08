# !#/usr/bin/python2.7.12
# # Author: Karthika K   
# # Name: e3.py          
# # Date: 30-Nov-2017 
"""Description:What is the largest prime factor of the number 600851475143"""   
def max_factor(num):
	i=2
	while(i<num):
		while(num%i)==0:
			num=num/i
			i=i+1
	if(num>1):
		return num
		return i
print max_factor(13195)





		