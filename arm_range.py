#Find Armstrong Numbers Between Two Intervals
#This python program will identify the Armstrong number between two intervals ,
 #the user is required to insert integer numbers. As we know about what are Armstrong Numbers? 
 #A Armstrong number is one which have the sum of its digits raised to their cube equal to itself. 
 #In this program, User have to enter two number such as start and end number. 
 #Then, we will write some conditions through which we will find how to find Armstrong Numbers.

#For example:
#13+53+33 = 153

#Basically we know that Armstrong number in given range 150 to 160  is only 153.  
#All other numbers are not Armstrong Number

import math

first = int(input("Enter first number:"))
second = int(input("Enter second number:"))


def is_Armstrong(val: int) -> bool:
    sum = 0
    arr = [int(d) for d in str(val)]
    for i in range(0, len(arr)):
        sum = sum + math.pow(arr[i], len(arr))
    if sum == val:
        print("{} number is Armstrong".format(val))
    else:
        print("{} number is not Armstrong".format(val))

for i in range(first, second + 1):
    is_Armstrong(i)


