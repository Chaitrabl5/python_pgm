#Decimal to binary conversion in Python
#Here, in this page we will discuss the program for decimal to binary conversion in python. 
# A decimal number is a standard representation of integers or non-integers, decimal numbers are also 
# called as numbers with base 10. Whereas in binary number system numbers are with base 10 and shows
#  representation by 0 and 1. In this program, we will convert decimal number to binary number by using 
# in-built bin() function.

#Example:9

#1) 9/2, Remainder = 1, Quotient = 4, 

#2) 4/2, Remainder = 0, Quotient = 2    

#3) 2/2, Remainder = 0, Quotient = 1, 

#4) 1/2, Remainder = 1, Quotient = 0

     #   9 in decimal = 1001 in binary

#take decimal number
dec_num = 124
#convert decimal number to binary
bin_num = bin(dec_num)
#print number
print('Number after conversion is :' + str(bin_num))


