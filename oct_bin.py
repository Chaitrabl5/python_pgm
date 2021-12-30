#Octal To Binary Conversion in Python
#Here, in this page we will discuss the program for octal to binary conversion in Python .
 #Numbers with base 8 are called octal numbers and uses digits from 0-7 for representation of octal number.
 # Where as numbers with base 2 are called binary numbers  and it uses 0 and 1 for representation of binary 
 # numbers.In python when a number starts from 0o[zero and o/O], it is considered as octal number and same with
 #  binary if a number starts with 0b[zero and b/B] it is called binary number. In this Python program we will 
 # convert a number 
#with base 8 to number with base 2 ie, from octal to binary.

#octal number with prefix 0o/0O
oct_num = 0o564
#using bin() to convert octal number to binary
bin_num = bin(oct_num)
#print binary Number
print('Number after conversion is :' + str(bin_num))