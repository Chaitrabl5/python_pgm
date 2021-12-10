#Factorial of number in Python
#In this Python Program, We will find the factorial of a number where the number should be entered by the user. Factorial of a number means multiply of all below number with each other till 1. If user enter 0 or 1 , then factorial of both numbers will be 1 only. Or If user enters negative numbers then it’s factorial is not defined.
#For Example:

#Number is 8.
#8x7x6x5x4x3x2x1=40,320
#Factorial of a 8 = 40,320

#Note:-Factorial of n number is 1*2*3*…n. You will learn to calculate the factorial of a number using for loop in this example

num = int(input("Enter the number:"))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i

print("Factorial of a Given Number:", factorial)


