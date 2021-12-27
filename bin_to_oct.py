#Binary to Octal Conversion in Python
#Here, in this section we will discuss the binary to octal conversion in Python.
# Binary numbers are also known as bits that represent 0 means FALSE and 1 means TRUE,
#  but usually binary numbers are with base 2 and can represent any number in form of 0 and 1. 
# Whereas Octal numbers expressed with base 8 and can represent any number with 0 to 7. 
# In this python program, we will convert binary numbers to octal numbers using oct() function.

#Example : The Binary number 110010101 is equivalent to 645 in Octal base

#take binary number
Bin_num = 0b10111
#convert using oct() function
Oct_num = oct(Bin_num)
#print number
print('Number after conversion is :' + str(Oct_num))