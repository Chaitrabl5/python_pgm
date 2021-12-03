#Sum of numbers in a given range
#In this article we will see a python program to add numbers present between a given range. User need to enter upper limit and lower limit. 

#For better understanding let’s suppose two values 3 and 8,

#Then, Sum of all natural numbers between 3 and 8 will be (3+4+5+6+7+8) = 33.

#So we will create a python program to calculate the sum of all natural numbers in a given range.

#Get the lower limit from user
lower_limit = int(input("Enter Lower limit: "))

#get upper limit from user
Upper_limit = int(input("Enter Upper limit: "))

#initialize submission as zero
sum=0

#iterate from lower to upper limit and add the numbers to sum.
for i in range(lower_limit,Upper_limit+1):
    sum=sum+i

#print sum value
print("Addition of numbers = ",sum)



