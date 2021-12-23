#HCF of two numbers
#Here, in this section we will discuss HCF of two numbers in python. 
#The HCF or the Highest Common Factor of two numbers is the largest common factor of two or more values.

#GCD i.e. Greatest Common Divisible or HCF i.e. 
#Highest Common Factor of two numbers is the largest positive integer that can divide both the numbers

#There are many methods to calculate GCD:

#Using Prime Factorisation,
#Euclid’s Algorithm,
#Lehmer’s GCD algorithm, etc
#Here we will use Euclid’s Algorithm to find the GCD, which is based on the idea that the GCD doesn’t 
#change when smaller number is subtracted from the greater number. This keeps on going until only the GCD left.

num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second Number:"))
arr = []
if num1 > num2:
    smaller = num2
else:
    smaller = num1
for i in range(1,smaller+1):
    if (num1 % i == 0) and (num2 % i == 0):
        arr.append(i)
print("The HCF of given numbers: {}".format(max(arr)))



