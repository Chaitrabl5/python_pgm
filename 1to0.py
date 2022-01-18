#Replace all 0’s With 1 in given integer
#Here we will discuss how to replace all the 0’s with 1 in a given integer.

#The concept is simple, find the digits of the integer. 
# Compare each digit with 0 if the digit is equal to 0 then replace it with 1. 
# Construct the new integer with the replaced digits.

#Example :
#n=12090 -> 12191
n=int(input("Enter any number"))

s=str(n)

l=[]

for i in s:

    if(i=='0'):

        l.append('1')

    else:

        l.append(i)

ns=""

for i in l:

    ns+=i

print(int(ns))


