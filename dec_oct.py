#Decimal to octal conversion
#Here, in this section we will discuss the program for decimal to octal conversion in python. 
# \Decimal numbers are the standard representation for representing integer or non-integer values.
#  Decimal numbers are with base 10 and can represent numbers from 0-9. Whereas in Octal representation of 
# numbers, numbers from 0-7 are represented as octal numbers are with base 8. In this python program, 
# we will convert decimal numbers to octal numbers using oct() function.



#take decimal number
Dec_num = 598
#convert using oct() function
Oct_num = oct(Dec_num)
#print number
print('Number after conversion is :' + str(Oct_num))