#Factors of number
# In this Python Program we will calculate the factors of given number. 
# The factors of a number can be calculated with the help of for loop starting from 1 to number
#  itself in which range original number divided by 1 to number itself which number divides the original
#  number completely. That number will be the factor of the original number.

#For Example:
#Number : 16
#Factors: 1, 2, 4, 8, 16

number = int(input("Enter the Number:"))
for i in range(1, number+1):
    if number % i == 0:
        print(i, end=" ")

# This code is contributed by Shubhanshu Arya (Prepinsta Placement Cell Student) 