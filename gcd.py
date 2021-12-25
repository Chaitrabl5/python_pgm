#GCD of two numbers in Python
#Here, in this section we will discuss GCD of two numbers in python. 
# Basically the GCD (Greatest Common Divisor) or HCF (highest common factor ) of two number is the 
# largest positive integer that divides each of the integers where the user entered number should not be zero.

#GCD i.e. Greatest Common Divisible or HCF i.e. Highest Common Factor of two numbers is the largest positive
#  integer that can divide both the numbers entered by the user.

#There are many methods to calculate GCD:

#Using Prime Factorisation,
#Euclid’s Algorithm,
#Lehmer’s GCD algorithm, etc

num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))


def gcdFunction(num1, num2):
    if num1 > num2:   
        small = num2
    else:
        small = num1
    for i in range(1, small+1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd = i
    print("GCD of two Number: {}".format(gcd))

gcdFunction(num1, num2)