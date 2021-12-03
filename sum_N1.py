### Find the sum of first N natural numbers
#Here we will discuss how to find the Sum of N Natural Numbers in python programming language, N being the limit which user will define.

#All the positive integers (1, 2, 3, 4…) are the Natural Numbers.

#Formula To find the sum of first N Natural Numbers 

          #  Sum = N(N+1)/2*

num = int(input("Enter the Number:"))
sum = (num * (num+1))/2
print("The Sum of N natural Number is {}".format(sum))
