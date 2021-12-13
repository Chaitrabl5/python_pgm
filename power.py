#Find Power of a Number
#In this Python program we will calculate the power of a number.
 #This program will ask two user inputs, one as base and second is power. 
 #So, we have to multiply base value itself with particular number of times which is given as power.

#For Example:

#Base: 5
#Expo: 2
#Calculation: 5 * 5
#Result: 25

base = int(input("Enter Base number:"))
expo = int(input("Enter Expo Number:"))
temp = 1

for i in range(0, expo):
    temp = temp * base

print(temp)
