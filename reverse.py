#Reverse of a given number
#In this Python program we are finding the reverses of a number entered by a user and then print it. For finding the result, we have to use a variable and initialize it. Run while loop until condition gets false. and then finally print the result.
#For example:
#Enter the Number: 1568
#Reverse of a Number: 8651
num = int(input("Enter the Number:"))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print("The Given number is {} and Reverse is {}".format(temp, reverse))