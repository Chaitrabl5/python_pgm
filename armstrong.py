#Armstrong or not in Python
#A Armstrong number is one which have the sum of its digits raised to their cube equal to itself

#For Example: –
#Enter any number 1634.
#14 + 64 + 34 + 44 = 153

#Number is Armstrong
import math
value = int(input("Enter the Number: "))
num = [int(d) for d in str(value)]
sum = 0
for i in range(0, len(num)):
    sum = sum + math.pow(num[i], len(num))

if sum == value:
    print("Given number is Armstrong Number")
else:
    print("Given Number is not Armstrong Number")




