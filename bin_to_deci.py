#Binary to Decimal Conversion
#In this article we will discuss binary to decimal conversion in Python.
#  For this purpose we need to take a binary integer number from user and convert that binary integer number 
# to its decimal equivalent form and then print the converted number on to the screen. 
# A Decimal number can be calculated by multiplying every digits of binary number with 2 to the power of 
# the integers starts from 0 to n-1 where n refers as the total number of digits present in a binary number and 
# finally add all of them.

#In number system, Binary number contains only two digits of 0, 1 which has base 2.
#  Whereas Decimal Number contains only 10 Symbols: 0, 1, 2, 3, 4, 5, 6, 7 , 8 and 9 which has base 10.

#For example:

#101 in base 2(Binary) => 5 in base 10(decimal)

#100101 in base 2(Binary) => 37 in Base 10 (Decimal)


num = int(input("Enter number:"))
binary_val = num
decimal_val = 0
base = 1
while num > 0:
    rem = num % 10
    decimal_val = decimal_val + rem * base
    num = num // 10
    base = base * 2

print("Binary Number is {} and Decimal Number is {}".format(binary_val, decimal_val))
