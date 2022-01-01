#Octal To Decimal Conversion
#Here, in this page we will discuss the program for octal to decimal conversion in python .
#  Octal numbers are also called numbers with base 8 and hold values from 0 – 7. 
# Whereas in Decimal numbers are with base 10 is Standard number system for denoting integers and non-integers.
#  In programing languages octal numbers are represented with 0o/0O[zero and o/O] in prefix and decimal numbers
#  are represented as normal integer representation.
#In this python program we will convert octal numbers into Decimal numbers or from a number with base 8 to 
# number with base 10.

#take octal number
#with prefix 0o[zero and o/O]
oct_num = 0o512
#convert octal number to integer
#integers are with base 10
deci_num = int(oct_num)
#print number
print('Number after conversion is :' + str(deci_num))
