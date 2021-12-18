
#Perfect number is a positive integer that is equal to the sum of its proper divisors. In this program we will be checking whether the given number is perfect or not using for loop. Initially we will be finding the proper divisors of the number and then we will find the sum of the divisors. If the sum is equal to the number, then the number is perfect.

#Example n=14
#Proper divisors of 14 are 1,2,7
#Sum of the divisors is 10
#14 is not a perfect number

n = int(input("Enter any number: "))
sun = int(input("Enter any number: "))
sump= 0
for i in range(1, n):
    if(n % i == 0):
        sump= sump + i
if (sump == n):
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")mp= 0
for i in range(1, n):
    if(n % i == 0):
        sump= sump + i
if (sump == n):
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")


