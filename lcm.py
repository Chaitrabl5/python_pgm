#LCM of two numbers in Python
#Here, in this section we will discuss the LCM of two numbers in python.
#In this Python Program find the LCM of Two Numbers which numbers are entered by the user.
#  Basically the LCM of two numbers is the smallest number which can divide the both numbers equally. 
# This is also called Least Common Divisor or LCD.

#Let up suppose, we have two numbers, 60 and 72
#LCM = 2 * 2 * 2 * 3 * 3 * 5
#Result : 360 as the LCM of both Numbers.


num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second Number:"))


def lcmFinder(num1, num2):
    if num1 > num2:
        larger = num1
    else:
        larger = num2
    while True:
        if (larger % num1 == 0) and (larger % num2 == 0):
            lcm = larger
            break
        larger = larger + 1
    print("LCM of two given number:{}".format(lcm))


lcmFinder(num1, num2)
